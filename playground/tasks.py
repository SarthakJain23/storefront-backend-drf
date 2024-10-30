from time import sleep

from celery import shared_task
from templated_mail.mail import BaseEmailMessage


@shared_task
def notify_customers(msg):
    print("Sending message to all customers:", msg)
    for i in range(5000):
        print(f"{i}th message sent")
        message = BaseEmailMessage(
            template_name="email/hello.html",
            context={"name": f"Sarthak_{i}"},
        )
        message.send([f"sarthak_{i}@carefi.in"])

    print("Message sent to all customers:", msg)
