from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
import requests
from django.core.files.base import ContentFile

CustomUser = get_user_model()

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        profile_pic_url = None
        if sociallogin.account.provider == 'GitHub':
            profile_pic_url = sociallogin.account.extra_data.get('avatar_url')
        elif sociallogin.account.provider == 'Google':
            profile_pic_url = sociallogin.account.extra_data.get('picture')

        if profile_pic_url:
            try:
                response = requests.get(profile_pic_url)
                if response.status_code == 200:
                    file_name = f"{user.username}_profile_pic.jpg"
                    user.profile_pic.save(file_name, ContentFile(response.content), save=True)
            except Exception as e:
                print(f"Rasmni saqlashda xatolik: {e}")

        return user