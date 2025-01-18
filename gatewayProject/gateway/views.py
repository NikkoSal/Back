import requests
from django.http import HttpResponse


def proxy_request(request):
    url = "http://127.0.0.1:8000/myapp6/"

    response = requests.get(url)

    return HttpResponse(
        response.text,
        status=response.status_code,
        content_type=response.headers.get('Content-Type', 'text/plain')

    )