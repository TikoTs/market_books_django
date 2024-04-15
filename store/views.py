from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from store.models import Book, Category


def book_list(request):
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 3)
    # getting page parameter
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "store_home.html", {"page_obj": page_obj})


def get_book(request, book_id):
    book = get_object_or_404(Book.objects.prefetch_related("categories"), id=book_id)
    return render(request, "book_details.html", {"book": book})
