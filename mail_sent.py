from datetime import datetime
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ftp_admin.settings')

django.setup()

from client.models import Client
from django.core.mail import send_mail

# Get all of the user
clients = Client.objects.all()

for client in clients:
    
    date_diff = int((client.expire.date() - datetime.now().date()).days)
    if(date_diff == 7):
        
        message = Mail(
            from_email='movply@gmail.com',
            to_emails='abuanwar072@gmail.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content=f"<h3>Dear {client.first_name}</h3> <br /><p>Plz Renew your account only 7 days left</p>")
        try:
            sg = SendGridAPIClient(
                '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')
            response = sg.send(message)

        except Exception as e:
            print(e)
        print('Sent mail that he had 7 days left')
    elif(date_diff == 0):
        print('He Already expired, we give him 5 days more to pay the bill')
    elif(date_diff == -5 ):
        print('Your package expired and you are not getting any update anymore')
