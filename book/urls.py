from django.contrib import admin
from django.urls import path
from book.views import AutherListView,AutherDetailView,BooksListView,BooksDetailView

urlpatterns = [
    path('authors/', AutherListView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AutherDetailView.as_view(), name='author-detail'),
    path('books/', BooksListView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BooksDetailView.as_view(), name='book-detail'),
]