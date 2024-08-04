##rest framework realted
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# auth related
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# filters related
from rest_framework import generics
from django_filters.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


####### import within app
from .models import Post,Profile
from .serializers import UserSerializer,PostSerializer,ProfileSerializer

## global imports, installed apps
import jwt,datetime,django_filters
from django.shortcuts import render

# exceptions
from rest_framework.exceptions import AuthenticationFailed

#resetpassword related
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


# RestPassword==> 1. /=> clicking resertpassword, 2.=> sending him resetpassword

class PasswordResetRequestView(APIView):
      def post(self, request):
          email = request.data['email']
          user = User.objects.get(email=email)
          
          if not user:
              return Response({'messsage':'User not registered, please signup'})
          
          refresh = RefreshToken.for_user(user)
          token = str(refresh.access_token)
          current_site = get_current_site(request)
          mail_subject = 'Reset Password'
          email_from = settings.EMAIL_HOST_USER
          message = render_to_string('password_reset_email.html',{
              'user':user,
              'domain':current_site,
              'token':token
            })
        #   print(message)
          send_mail(mail_subject,message,email_from,[email])
          return HttpResponse('Email sent successfully')
      
class PasswordResetConfirmView(APIView):
    def get(self, request):
        token = request.query_params.get('token')
        
        if not token:
            return Response({'message':"Invalid token, Please use Reset Password again"})
        
        acess_token = AccessToken(token)
        user_id = acess_token['user_id']
        user = User.objects.get(id=user_id)
        # print("acceess", acess_token)
        return render(request,'password_reset_form.html',{'token':token})
    
    def post(self, request):
        print(request.data)
        password = request.data['password']
        confirm_password = request.data['password_confirm']
        token = request.data['token']
        if not token:
            return Response({'message':"Invalid token, Please use Reset Password again"})
        
        acess_token = AccessToken(token)
        user_id = acess_token['user_id']
        user = User.objects.get(id=user_id)
        print("user", user)
        if password==confirm_password:
            user.set_password(password)
            user.save()
            print(password,confirm_password,token)
            return Response({'message':"Password reset sucessfully"})
        return Response({'message':"Something went wrong"})
        
     
 
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile(user=user, user_type = request.data.get('user_type'))
            profile.save()
            return Response({'message':"Signup Sucessfull", 'user_details': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message':"Invalid Credentials"}, status=status.HTTP_406_NOT_ACCEPTABLE)

class LoginView(APIView):
     def post(self, request):
         username = request.data.get('username')
         password = request.data.get('password')
         
         user = User.objects.filter(username=username).first()
         print(username,password,user)
         if user is None:
             return Response({'message':'User not Regitsered, Please Signup'}, status=status.HTTP_404_NOT_FOUND)
         
         if not user.check_password(password):
             return Response({'message':'wrong password, Please try again'}, status=status.HTTP_400_BAD_REQUEST)
         # i will create a token here, where i will hide the information of logged in user
         login(request,user)
         payload = {
             'id':user.id,
             'exp': datetime.datetime.now(datetime.UTC)+datetime.timedelta(minutes=60),
             'iat':datetime.datetime.now(datetime.UTC)
         }
         token = jwt.encode(payload,'cap1.4b', algorithm='HS256')
         print(token)
         response = Response()
         response.data = {'message':'login sucessfull','token':token}
         response.satus = status.HTTP_200_OK
         response.set_cookie(
             key='jwt',
             value=token,
             httponly=False,
             samesite=None,
             secure=None
         )
         return response
     
class PostView(APIView):
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'message':"Here is the list of posts", 'data':serializer.data},status=status.HTTP_200_OK)
        
    def post(self, request):
        print("from view", request.author)
        print("from view2", request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            print("s", serializer.validated_data)
            serializer.validated_data['author'] = request.author
            serializer.save()
            return Response({'message':'Post Added'}, status=status.HTTP_201_CREATED)
        return Response({'message':'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request,*args, **kwargs):        
        post_id = kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        print("post", post)
        serializer = PostSerializer(post, data=request.data,partial =True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Post Updated', "updated_post": serializer.data}, status=status.HTTP_200_OK)
        return Response({'message':'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,*args, **kwargs):        
        post_id = kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        print("post", post)
        post.delete()
        return Response({'message':'Post Deleted'}, status=status.HTTP_200_OK)

class PostFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author__user__username', lookup_expr='iexact')
    published = django_filters.BooleanFilter(field_name='publihsed')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains') 
    class Meta:
        fields = ['author', 'published', 'title']
        
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000
        
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().select_related('author').prefetch_related('author__user')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['author', 'title', 'publihsed']  # Adjust as per your model fields
    ordering_fields = ['created_at', 'updated_at','title']  # Add other fields for ordering if needed
    filterset_class = PostFilter
    pagination_class = CustomPagination