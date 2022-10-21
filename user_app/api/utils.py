from django.core.mail import EmailMessage
import os


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['mail_to']])
        email.send()
