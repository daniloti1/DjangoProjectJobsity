from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User

from .labels import *
import requests

s = requests.Session()

def requestApi(request, route, method='GET', data={}, files=None, json={}):
    try:
        url = settings.API_ROOT_DIR+route
        req = requests.Request(method, url, data=data, files=files, json=json)
        resp = s.send(s.prepare_request(req))
        data = resp.json()
    except Exception as e:
        data = {"detail": "There was a problem with the connection, please try again later", "error": 1}
    return JsonResponse(data)

def validateRelationship(request):
    data = {"detail": "Invalid user", "error": 1}
    try:
        userId = request.POST.get('user', request.user.id)
        user = User.objects.get(id=userId)
        if not user:
            return JsonResponse(data)
    except Exception as e:
        return JsonResponse(data)
    return None
    