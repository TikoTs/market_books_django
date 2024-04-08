from django.contrib import admin
from store.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("book_name", "page_count", "category", "author", "price", "image")
    search_fields = ("book_name", "author")


admin.site.register(Book, BookAdmin)
