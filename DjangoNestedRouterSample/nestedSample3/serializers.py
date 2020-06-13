from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title')
