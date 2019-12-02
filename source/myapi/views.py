import json
import math
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# def api_example(request, *args, **kwargs):
#     request_data = None
#     if request.body:
#         request_data = json.loads(request.body)
#     data = {
#         'method': request.method,
#         'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#         'content': request_data
#     }
#     return JsonResponse(data)

@csrf_exempt
def add_view(request, *args, **kwargs):
    request_data = None
    sum = 0
    if request.body:
        request_data = json.loads(request.body)
        for data in request_data:
            try:
                sum += request_data[data]
            except TypeError:
                return JsonResponse({'error': 'data is not a digit'})

        data = {
           'answer': sum
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'body is empty'})


def divide_view(request, *args, **kwargs):
    pass


def multiply_view(request, *args, **kwargs):
    pass


def subtract_view(request, *args, **kwargs):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
        for data in request_data:
