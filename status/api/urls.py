""" statusModelAPIs URL Configuration """

from django.conf.urls import url

from .views import (StatusAPIView,
                    StatusAPIDetailView,
                    # StatusListSearchAPIView,
                    # StatusCreateAPIView,
                    # StatusDetailAPIView,
                    # StatusUpdateAPIView,
                    # StatusDeleteAPIView,
                    )

urlpatterns = [

    url(r'^$', StatusAPIView.as_view()),

    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),

    # url(r'^$', StatusListSearchAPIView.as_view()),

    # url(r'^create/', StatusCreateAPIView.as_view()),

    # url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),

    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),

    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),

]
