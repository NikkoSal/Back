import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

FIRST_SERVER_URL = "http://127.0.0.1:8000"

@csrf_exempt
def proxy(request, subpath):
    url = f"{FIRST_SERVER_URL}/{subpath}"

    method = request.method
    data = request.body
    headers = {key: value for key, value in request.headers.items() if key != 'Host'}

    try:
        response = requests.request(method, url, headers=headers, data=data)
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers.get('Content-Type'))
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def home(request):
    return HttpResponse('<h1>Добро пожаловать!</h1>')
