import random
from email.header import Header

from django.core.mail import send_mail
from django.utils import timezone

from account.models import EmailVerification


def send_verification_code(email):
    code = str(random.randint(100000, 999999))  # کد ۶ رقمی
    EmailVerification.objects.update_or_create(
        email=email,
        defaults={'code': code, 'created_at': timezone.now()}
    )

    send_mail(
        subject="کد تأیید ثبت‌نام",
        message=f"کد شما: {code}",
        from_email="kiarashgholami1383@gmail.com",
        recipient_list=[email],
    )
