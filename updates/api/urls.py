""" UpdateModelAPIs URL Configuration """

from django.conf.urls import url

from updates.api.views import (UpdateModelDetailAPIView,
                               UpdateModelListAPIView,
                               )

urlpatterns = [
    url(r'^$', UpdateModelListAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()),
]
