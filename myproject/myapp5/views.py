from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

@login_required
def view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'view.html', {'user': user})

@login_required
def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            User.objects.create_user(username=username, password=password)
            return redirect('users')
        else:
            return render(request, 'edit.html')

    return render(request, 'edit.html')

@login_required
def edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username:
            user.username = username
        if password:
            user.set_password(password)
        user.save()
        return redirect('users')

    return render(request, 'edit.html', {'user': user})

@login_required
def delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('users')

    return render(request, 'delete.html', {'user': user})
