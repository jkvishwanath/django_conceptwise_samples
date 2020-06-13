from django.conf.urls import url, include
from django.contrib import admin
from nestedSample4.api import router
#https://apptension.com/blog/2017/09/13/rest-api-using-django-rest-framework/

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api2/', include(router.urls))
]
