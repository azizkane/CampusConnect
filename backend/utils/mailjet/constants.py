""" Auteur: akane
    Date: 23/10/2024
    Description: ---------------------
"""


import os
from dotenv import load_dotenv
from mailjet_rest import Client

load_dotenv()

NAME ="Aziz Kane"
DEFAULT ="akane@softvalleylabs.com"
BACKEND ='mailjet_rest.EmailBackend'

API_KEY = str(os.getenv('MAILJET_API_KEY'))
SECRET_KEY = str(os.getenv('MAILJET_SECRET_KEY'))

TEMPLATES={
    'ACCOUNT_ACTIVATION' :6404020,
    'PASSWORD_RESET' : 6391569,
}

##############################################


class MailjetClient:
    def __init__(self):
        self.client = Client(auth=(API_KEY, SECRET_KEY), version='v3.1')

# Create a Mailjet client instance
mailjet_client = MailjetClient().client



