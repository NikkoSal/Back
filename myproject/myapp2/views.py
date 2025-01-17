from django.shortcuts import render
from django.http import HttpResponse

def post1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Привет, {name}!')
    return render(request, 'form.html')

def post2(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1','0')
        num2 = request.POST.get('num2','0')
        res = int(num1) + int(num2)
        return HttpResponse (f'Результат: {res}')
    return render(request, 'sum.html')

def get(request):
    query = request.GET.get('q', '')
    return render(request, 'search.html', {'query': query})