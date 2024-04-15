from pathlib import Path
from django.db import models
from django.utils.translation import gettext_lazy as _
from store.data.enums import CoverTypeEnum


class Book(models.Model):
    book_name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name=_("Book Name")
    )
    book_cover_type = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in CoverTypeEnum],
        default=None,
        verbose_name=_("Book Cover Type"),
    )
    page_count = models.IntegerField(null=True, verbose_name=_("Page Count"))
    categories = models.ManyToManyField("Category", verbose_name=_("Categories"))
    author = models.ForeignKey(
        "Author", on_delete=models.SET_NULL, null=True, verbose_name=_("Author")
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, verbose_name=_("Price")
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=Path("book_cover_images"),
        verbose_name=_("Image"),
    )

    def __str__(self):
        return self.book_name

    class Meta:
        db_table = "store_book"
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Author Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
