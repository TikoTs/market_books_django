from django.shortcuts import render
from store.models import Book


def get_books(request):
    return render(
        request, "store_home.html", {"books": Book.objects.all(), "user": request.user}
    )


def get_book(request, book_id):
    return render(request, "book_details.html", {"book": Book.objects.get(id=book_id)})
