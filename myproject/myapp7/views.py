from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp4.models import User
from .forms import EmailForm

@login_required
def send_password_email(request):
    user = request.user

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'] 
            subject = 'Ваш пароль'
            message = f'Ваш пароль: {user.password}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            return render(request, 'password_sent.html', {'email': email})
    else:
        form = EmailForm()

    return render(request, 'email_form.html', {'form': form})

