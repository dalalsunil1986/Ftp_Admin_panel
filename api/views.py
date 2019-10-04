from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

send_mail(
    'Property Listing Inquiry',
    f'There has been an inquiry for. Sign in to your account for more.',
    'movplys@gmail.com',
    ['abuanwar072@gmail.com', '24hdvideo@gmail.com'],
    fail_silently=False,
)
