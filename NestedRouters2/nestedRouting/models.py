from django.db import models

# Create your models here.
class TestResource(models.Model):
	name = models.CharField(max_length=255)
	active = models.BooleanField(default=True)

class NestedResource(models.Model):
	name = models.CharField(max_length=255)
	resource = models.ForeignKey(
		'TestResource', on_delete=models.CASCADE)


