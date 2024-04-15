from django.contrib import admin
from store.models import Book, Author, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ("book_name", "author", "price", "display_categories")

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    display_categories.short_description = "Categories"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
