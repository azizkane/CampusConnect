""" Auteur: akane
    Date: 24/10/2024
    Description: ---------------------
"""

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from mailjet.constants import*

def send_template_email(user,to_name, subject, template_id, variables, mailjet=mailjet_client):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": DEFAULT,
                    "Name": NAME
                },
                "To": [
                    {
                        "Email": user.email,
                        "Name": to_name,
                    }
                ],
                "TemplateID": template_id,
                "TemplateLanguage": True,
                "Subject": subject,
                "Variables": variables
            }
        ]
    }

    result = mailjet.send.create(data=data)
    return result.status_code



def send_email(user,to_name, subject, template_id, context, variables, mailjet=mailjet_client):
    # Render HTML content using Django templates
    html_content = render_to_string(template_id, context)
    # Optionally generate plain text content
    text_content = strip_tags(html_content)
    mailjet
    data = {
        'Messages': [
            {
                'From': {
                    'Email': DEFAULT,
                    'Name': NAME
                },
                'To': [
                    {
                        'Email': user.email,
                        'Name':to_name ,
                    }
                ],
                'Subject': subject,
                'TextPart': text_content,
                'HTMLPart': html_content,
                "Variables": variables,
                # You can include 'CustomID' or other Mailjet options here
            }
        ]
    }

    result = mailjet.send.create(data=data)
    return result.status_code
