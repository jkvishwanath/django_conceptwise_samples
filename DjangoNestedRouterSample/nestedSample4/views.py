from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BookSerializer, EditionSerializer
from .models import Author, Book, Edition

from rest_framework_extensions.mixins import NestedViewSetMixin



class AuthorViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class EditionViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = EditionSerializer
    queryset = Edition.objects.all()
