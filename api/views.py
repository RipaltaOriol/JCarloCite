import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

# TODO: delete this for production
@csrf_exempt
def upload_file(request, *args, **kwargs):
    if request.method == "POST":
        file = request.FILES['file_name']
        # handle the file logic [Nico]
        # ...
        # ...
        return JsonResponse({"message": "its a post"})
    return JsonResponse({"message": "Wrong path..."})