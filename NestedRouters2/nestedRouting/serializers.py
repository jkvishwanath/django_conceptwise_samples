from rest_framework.serializers import HyperlinkedModelSerializer
#from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from .models import TestResource,NestedResource
from drf_nested_routing.serializers import NestedRoutingSerializerMixin

class TestResourceSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = TestResource
		fields = '__all__'

class NestedResourceSerializer(NestedRoutingSerializerMixin, HyperlinkedModelSerializer):
	class Meta:
		model = NestedResource
		fields = '__all__'
