from django.urls import path
from .views import IndexView, LoginView, RegisterView, LogoutView, SettingsView, send_verification_email, verify_email, chat_with_user

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('send-verification-email/', send_verification_email, name='send_verification_email'),
    path('verify-email/', verify_email, name='verify_email'),
    path("chat/<int:user_id>/", chat_with_user, name="chat_with_user"),
]