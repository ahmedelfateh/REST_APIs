from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse


class UpdateModelDetailAPIView(View):
    def get(self, resquest, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, resquest, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')

    def put(self, resquest, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')

    def delet(self, resquest, *args, **kwargs):

        return HttpResponse({}, content_type='application/json')


class UpdateModelListAPIView(View):
    def get(self, resquest, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, resquest, *args, **kwargs):
        data = json.dumps({"message": "Unknown data"})
        return HttpResponse(data, content_type='application/json')

    def delete(self, resquest, *args, **kwargs):
        data = json.dumps({"message": "You can't delete the entire list"})
        return HttpResponse(data, content_type='application/json')
