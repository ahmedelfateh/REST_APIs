import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.core.serializers import serialize

# import models here
from .models import Update

# import mixins here
from DjangoAPIs.mixins import JsonResponseMixin

# Create your views here.


def update_detail_view_JsonResponse(request):
    '''using django JsonResponse'''
    # # http://127.0.0.1:8000/jsonres/
    data = {
        "count": 1000,
        "content": "using django JsonResponse"
    }
    return JsonResponse(data)


def update_detail_view_json(request):
    '''using python json lib'''
    # # http://127.0.0.1:8000/json/
    data = {
        "count": 1000,
        "content": "using python json lib"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class update_detail_view_CBV(View):
    '''using django JsonResponse with CBV'''
    # # http://127.0.0.1:8000/jsonCBV/

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "using django JsonResponse with CBV"
        }
        return JsonResponse(data)


class update_detail_view_CBV_mixin(JsonResponseMixin, View):
    '''using django JsonResponse with CBV with mixin'''
    # # http://127.0.0.1:8000/jsonCBVmixin/

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "using django JsonResponse with CBV"
        }
        return self.render_to_json_response(data)


class update_detail_SerializedView(View):
    '''using django Serialize with CBV
    to get detail view from a actual database data '''
    # # http://127.0.0.1:8000/jsonSerializedDetailView/

    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj, ], fields=('user', 'content'))

        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class update_list_SerializedView(View):
    '''using django Serialize with CBV
    to get list view from a actual database data'''
    # # http://127.0.0.1:8000/jsonSerializedListView/

    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))

        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class update_detail_SerializedView_Model(View):
    '''using django Serialize with CBV
    to get detail view from a actual database data '''
    # # http://127.0.0.1:8000/jsonSerializedDetailViewModel/

    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)

        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')


class update_list_SerializedView_Model(View):
    '''using django Serialize with CBV
    to get list view from a actual database data
    get data from model'''
    # # http://127.0.0.1:8000/jsonSerializedListViewModel/

    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()

        json_data = Update.objects.all().serialize()

        return HttpResponse(json_data, content_type='application/json')
