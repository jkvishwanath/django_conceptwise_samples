from rest_framework.serializers import ModelSerializer
from .models import Author, Book,Edition


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title')

class EditionSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = ('id', 'book', 'year')
