from django.contrib import admin
from .models import User, Service

# admin.site.register(User)
admin.site.register(Service)
class UserAdmin(admin.ModelAdmin):
    search_fields=["name", "email"]
    list_filter=["gender"]

admin.site.register(User, UserAdmin)