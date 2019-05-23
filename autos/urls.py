from django.conf.urls import url
from rest_framework import routers
from autos.views import *

urlpatterns = [
    url(r'^auto/$', AutoList.as_view(),name='autoList'),
    url(r'^auto/(?P<pk>\d+)/?$', AutoList.as_view())
]