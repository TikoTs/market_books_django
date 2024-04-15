# Generated by Django 5.0.3 on 2024-04-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "Author", "verbose_name_plural": "Authors"},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name": "Book", "verbose_name_plural": "Books"},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="book",
            name="book_cover_type",
            field=models.CharField(
                choices=[("SOFT", "SOFT"), ("HARD", "HARD"), ("SPEC", "SPEC")],
                default=None,
                max_length=20,
                verbose_name="Book Cover Type",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_name",
            field=models.CharField(max_length=100, verbose_name="Book Name"),
        ),
    ]