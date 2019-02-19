from django.http import JsonResponse


class JsonResponseMixin(object):
    ''' this mixin work to convert any
    type of data into a dictionary before 
    passing it to the JsonResponse '''

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context
