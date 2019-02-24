""" DjangoAPIs URL Configuration """

from django.conf.urls import (url,
                              include)
from django.contrib import admin
from updates.views import (
    update_detail_view_JsonResponse, update_detail_view_json,
    update_detail_view_CBV, update_detail_view_CBV_mixin,
    update_detail_SerializedView, update_list_SerializedView,
    update_list_SerializedView_Model, update_detail_SerializedView_Model,)

from rest_framework_jwt.views import (obtain_jwt_token,
                                      refresh_jwt_token)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^api/updates/', include('updates.api.urls')),

    url(r'^api/status/', include('status.api.urls')),

    url(r'^api/auth/', include('accounts.api.urls')),

    # url(r'^api/auth/jwt/$', obtain_jwt_token),
    # url(r'^api/auth/jwt/refresh/$', refresh_jwt_token),

    # url(r'^jsonres/', update_detail_view_JsonResponse,
    #     name='update_detail_view'),
    # url(r'^json/', update_detail_view_json, name='update_detail_view_json'),
    # url(r'^jsonCBV/', update_detail_view_CBV.as_view(),
    #     name='jsonCBV'),
    # url(r'^jsonCBVmixin/', update_detail_view_CBV_mixin.as_view(),
    #     name='jsonCBVmixin'),
    # url(r'^jsonSerializedDetailView/', update_detail_SerializedView.as_view(),
    #     name='jsonSerializedDetailView'),
    # url(r'^jsonSerializedListView/', update_list_SerializedView.as_view(),
    #     name='jsonSerializedListView'),
    # url(r'^jsonSerializedDetailViewModel/', update_detail_SerializedView_Model.as_view(),
    #     name='jsonSerializedDetailViewModel'),
    # url(r'^jsonSerializedListViewModel/', update_list_SerializedView_Model.as_view(),
    #     name='jsonSerializedListViewModel'),
]
