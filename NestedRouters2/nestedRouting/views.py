from django.shortcuts import render
from.serializers import NestedResourceSerializer,TestResourceSerializer
from .models import NestedResource,TestResource
from rest_framework.viewsets import ModelViewSet
from drf_nested_routing.views import NestedViewSetMixin


# Create your views here.
class TestResourceViewSet(ModelViewSet):
	serializer_class = TestResourceSerializer
	queryset = TestResource.objects.all()
	all_fields = TestResourceSerializer.Meta.fields
	print(all_fields)

class NestedResourceViewSet(NestedViewSetMixin, ModelViewSet):
	serializer_class = NestedResourceSerializer
	queryset = NestedResource.objects.all()
	all_fields1 = NestedResourceSerializer.Meta.fields
	print(all_fields1)