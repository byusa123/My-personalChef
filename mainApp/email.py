from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def confirmation_email(first_name, last_name, schedule, receiver):
    # Creating message subject and sender
    subject = 'Booking Confirmation'
    sender = 'wemychef@gmail.com'

    # passing in the context vairables
    text_content = render_to_string('email.txt',
                                    {"first_name": first_name, "last_name": last_name, "schedule": schedule})
    html_content = render_to_string('email.html',
                                    {"first_name": first_name, "last_name": last_name, "schedule": schedule})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
