from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(
        'Author',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
