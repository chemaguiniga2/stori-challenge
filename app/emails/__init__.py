from django.conf import settings

from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_stori_email(context):
    html_message = render_to_string("content/email.html", context=context)
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject = "Stori Challenge", 
        body = plain_message,
        from_email = None ,
        to=settings.EMAIL_RECEIVERS
    )

    message.attach_alternative(html_message, "text/html")
    message.send()
