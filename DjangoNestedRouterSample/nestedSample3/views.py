from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

from rest_framework_extensions.mixins import NestedViewSetMixin



class AuthorViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
