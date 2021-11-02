from django.core.mail import send_mail
from test_django.celery import app


@app.task
def send_email(subject, text, email_from, email_to):
    send_mail(
        subject,
        text,
        email_from,
        [email_to],
        fail_silently=False,
    )
