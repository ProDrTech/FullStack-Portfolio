from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
import requests
from django.core.files.base import ContentFile
import logging

# Logging sozlamalari
logger = logging.getLogger(__name__)

CustomUser = get_user_model()

@receiver(social_account_added)
def save_profile_picture(request, sociallogin, **kwargs):
    user = sociallogin.user
    social_account = sociallogin.account
    profile_pic_url = None

    logger.info(f"Social account added for user: {user.username}")
    logger.info(f"Provider: {social_account.provider}")
    logger.info(f"Extra data: {social_account.extra_data}")

    if social_account.provider == 'Google':
        profile_pic_url = social_account.extra_data.get('picture')
        logger.info(f"Google profile picture URL: {profile_pic_url}")
    elif social_account.provider == 'GitHUb':
        profile_pic_url = social_account.extra_data.get('avatar_url')
        logger.info(f"GitHUb profile picture URL: {profile_pic_url}")

    if profile_pic_url:
        try:
            response = requests.get(profile_pic_url, stream=True)
            logger.info(f"Response status code: {response.status_code}")
            if response.status_code == 200:
                file_name = f"{user.username}_profile_pic.jpg"
                user.save()  # Foydalanuvchi obyekti saqlanishi uchun
                user.profile_pic.save(file_name, ContentFile(response.content), save=True)
                logger.info(f"Profile picture saved for user: {user.username}")
            else:
                logger.error(f"Failed to download image: {response.status_code}")
        except Exception as e:
            logger.error(f"Error saving image: {e}")
    else:
        logger.warning("No profile picture URL found")