from django.http import HttpResponse
import requests


with open(".env") as f:
    url = f.readline().strip()

def proxy_request(request):
    response = requests.get(url)

    return HttpResponse(
        response.text,
        status=response.status_code,
        content_type=response.headers.get('Content-Type', 'text/plain')
    )
