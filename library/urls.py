from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/borrow/', views.borrow_book, name='borrow_book'),
    path('borrowing_history/', views.borrowing_history, name='borrowing_history'),
]
