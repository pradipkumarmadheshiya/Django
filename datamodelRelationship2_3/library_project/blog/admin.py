from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields=["title", "content"]
    list_display=["title", "content", "createdAt", "updatedAt"]
    list_filter=["title"]
    # list_editable=[ "content"]

admin.site.register(Post, PostAdmin)