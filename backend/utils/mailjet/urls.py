""" Auteur: akane
    Date: 23/10/2024
    Description: ---------------------
"""


from django.urls import path
from django.views.generic import TemplateView
from .views.account_activation import *
from .views.password_reset import *


urlpatterns = [
    path(
        'account_activation/<uidb64>/<token>/',
        AccountActivationView.as_view(),
        name='account_activation'
    ),
    path(
        'password_reset/<uidb64>/<token>/',
        PasswordResetView.as_view(),
        name='password_reset'
    )
]
