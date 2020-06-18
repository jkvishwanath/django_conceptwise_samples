from .views import TestResourceViewSet,NestedResourceViewSet
from drf_nested_routing.routers import NestedRouterMixin
from rest_framework.routers import SimpleRouter
from django.conf.urls import url, include
from django.urls import path

class NestedSimpleRouter(NestedRouterMixin, SimpleRouter):
	pass

router = NestedSimpleRouter()
resourceRoute = router.register(r'test-resources', TestResourceViewSet)
resourceRoute.register(r'nested', NestedResourceViewSet, ['resource_id'])

urlpatterns = [
    url(r'^api2/', include(router.urls))
]
'''
urlpatterns = patterns(
	'',
	url(r'', include(router.urls)),
)
'''