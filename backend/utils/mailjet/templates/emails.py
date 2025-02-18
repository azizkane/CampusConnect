""" Auteur: akane
    Date: 24/10/2024
    Description: ---------------------
"""


from mailjet.tools.default import *
from mailjet.constants import (TEMPLATES)

# ID du template Mailjet pour l'activation de compte

def account_activation(user, activation_url):
    subject = "Activation de compte"
    to_name=f"{user.first_name} {user.last_name}"
    variables={
        "firstname": user.first_name,
        "lastname": user.last_name,
        "activation_url": activation_url
    }

    send_template_email(
        user,
        to_name,
        subject,
        TEMPLATES['ACCOUNT_ACTIVATION'],
        variables,
    )


def password_reset(user, password_reset_url):
    mailjet_client,
    subject = "Réinitialisation du mot de passe"
    to_name=f"{user.first_name} {user.last_name}"
    variables={
        "firstname": user.first_name,
        "lastname": user.last_name,
        "password_reset_url": password_reset_url
    }

    send_template_email(
        user,
        to_name,
        subject,
        TEMPLATES['PASSWORD_RESET'],
        variables,
    )