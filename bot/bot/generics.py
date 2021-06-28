from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User

import requests

s = requests.Session()

def requestApi(request, route, method='GET', data={}, files=None, json={}):
    try:
        url = settings.API_ROOT_DIR + route
        req = requests.Request(method, url , data=data, files=files, json=json)
        resp = s.send(s.prepare_request(req))
        try:
            data = resp.json()
        except Exception as e:
            data = {"data": str(resp.text)[:100], "error": 0}
    except Exception as e:
        raise e
        data = {"detail": "There was a problem with the connection, please try again later", "error": 1}
    return JsonResponse(data)
