from django.shortcuts import render
from book.models import Auther,Books
from book.serializer import AutherSerializer,BooksSerializer
from rest_framework import generics
# Create your views here.

class AutherListView(generics.ListCreateAPIView):
    queryset=Auther.objects.all()
    serializer_class=AutherSerializer


class AutherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Auther.objects.all()
    serializer_class=AutherSerializer

class BooksListView(generics.ListCreateAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer

    