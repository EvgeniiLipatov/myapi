import json
import math
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
                response = JsonResponse({'error': 'data is not a digit'})
                response.status_code = 400
                return response

        data = {
           'answer': sum
        }
        return JsonResponse(data)

    return JsonResponse({'error': 'body is empty'})

@csrf_exempt
def divide_view(request, *args, **kwargs):
    request_data = None
    keylist = []
    if request.body:
        request_data = json.loads(request.body)
        for key in request_data:
            keylist.append(key)

        for key in range(len(keylist)):
            if request_data[keylist[key+1]] != 0:
                try:
                    div = request_data[keylist[key]] / request_data[keylist[key+1]]
                except TypeError:
                    response = JsonResponse({'error': 'data is not a digit'})
                    response.status_code = 400
                    return response

                data = {
                    'answer': div
                }
                return JsonResponse(data)
            response = JsonResponse({'error': 'cannot divide by zero'})
            response.status_code = 400
            return response

    return JsonResponse({'error': 'body is empty'})

@csrf_exempt
def multiply_view(request, *args, **kwargs):
    request_data = None
    multiple = 1
    if request.body:
        request_data = json.loads(request.body)
        for data in request_data:
            try:
                multiple *= int(request_data[data])
            except ValueError:
                response = JsonResponse({'error': 'data is not a digit'})
                response.status_code = 400
                return response


        data = {
            'answer': multiple
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'body is empty'})


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    request_data = None
    keylist = []
    if request.body:
        request_data = json.loads(request.body)
        for key in request_data:
            keylist.append(key)

        for key in range(len(keylist)):
            try:
                subt = request_data[keylist[key]] - request_data[keylist[key + 1]]
            except TypeError:
                return JsonResponse({'error': 'data is not a digit'})
            data = {
                'answer': subt
            }
            return JsonResponse(data)
    return JsonResponse({'error': 'body is empty'})


