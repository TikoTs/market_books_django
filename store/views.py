from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from store.models import Book


def book_list(request):
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 3)
    # getting page parameter
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store_home.html', {'page_obj': page_obj})


def get_book(request, book_id):
    return render(request, "book_details.html", {"book": Book.objects.get(id=book_id)})
