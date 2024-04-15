from pathlib import Path
from django.db import models
from store.data.enums import CoverTypeEnum


class Book(models.Model):
    class Meta:
        db_table = "store_book"

    book_name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Book Names"
    )
    book_cover_type = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in CoverTypeEnum],
        default=None,
    )
    page_count = models.IntegerField(null=True, verbose_name="Page Count")
    categories = models.ManyToManyField(
        "Category", verbose_name="Categories"
    )  # Correct field name and removed default

    author = models.ForeignKey(
        "Author", on_delete=models.SET_NULL, null=True, verbose_name="Author"
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, verbose_name="Price"
    )
    image = models.ImageField(
        null=True, blank=True, upload_to=Path("images"), verbose_name="Image"
    )

    def __str__(self):
        return self.book_name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author Name")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")

    def __str__(self):
        return self.name
