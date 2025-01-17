from django.http import HttpResponse
from django.shortcuts import redirect, render

def endpoint(request):
    if request.method == "GET":
        return render(request, 'test.html')
    elif request.method == "POST":
        return redirect("redirected")

def redirected(request):
    return HttpResponse("redirect")
