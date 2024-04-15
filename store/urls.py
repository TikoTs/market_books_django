from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="store_home"),
    path("<int:book_id>-book-details/", views.get_book, name="book_details"),
]
