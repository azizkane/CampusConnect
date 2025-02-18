
""" Auteur: akane
    Date: 24/10/2024
    Description: ---------------------
"""

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse

def generate_activation_url(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_url = request.build_absolute_uri(
        reverse('account_activation', kwargs={'uidb64': uid, 'token': token})
    )
    return activation_url

def generate_password_reset_url(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = request.build_absolute_uri(
        reverse('password_reset', kwargs={'uidb64': uid, 'token': token})
    )
    return reset_url
