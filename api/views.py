import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body #.decode('utf-8')
    # print(request, body)
    data = {}
    try:
        data = json.loads(body)
    except Exception as e:
        print(e)
    print(data)
    return JsonResponse({"message": "first api endping reached"})