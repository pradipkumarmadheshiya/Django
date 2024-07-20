from django.contrib import admin
from .models import Book, Publisher

class BookAdmin(admin.ModelAdmin):
    readonly_fields=("isbn",)

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)