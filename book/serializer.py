from book.models import Auther,Books
from rest_framework import serializers

class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auther
        fields="__all__"

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"