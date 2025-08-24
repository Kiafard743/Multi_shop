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

    subject = str(Header("کد تأیید ثبت‌نام", "utf-8"))
    message = f"کد شما: {code}"
    from_email = str(Header("kiarashgholami1383@gmail.com", 'utf-8'))

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[email],
    )
