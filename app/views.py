from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.views import View
from users.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import HttpResponse
# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:index')
        return redirect('app:login')

class RegisterView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Ushbu email allaqachon ro'yxatdan o'tgan.")
            return render(request, 'login.html')

        if name and email and password:
            user = CustomUser(username=name, email=email)
            user.set_password(password) 
            user.save()
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz. Login qiling.")
            return redirect('app:login')
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('app:index')
    
class SettingsView(View):
    def get(self, request):
        request.user.refresh_from_db()
        return render(request, 'settings.html')

@login_required
def send_verification_email(request):
    user = request.user
    verification_link = request.build_absolute_uri(
        reverse('app:verify_email') + f"?user_id={user.id}"
    )

    subject = "Emailingizni tasdiqlang"
    message = f"Salom {user.username},\n\nEmailingizni tasdiqlash uchun quyidagi havolani bosing:\n{verification_link}\n\nRahmat!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    return HttpResponse("Tasdiqlovchi email yuborildi.")



def verify_email(request):
    user_id = request.GET.get("user_id")
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)
    
    user.email_verified = True
    user.save()

    return HttpResponse("✅ Email muvaffaqiyatli tasdiqlandi.")

