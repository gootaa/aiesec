from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail

from .tokens import account_activation_token

def send_activation_email(request, user):
    site_domain = get_current_site(request).domain
    protocol = request.scheme
    mail_subject = 'Activate Your Aiesec Account'
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    message = render_to_string('activation_mail.html',
                                {
                                    'user': user,
                                    'domain': site_domain,
                                    'protocol': protocol,
                                    'uid':uid,
                                    'token': token,
                                })
    send_mail(mail_subject, message, 'no-reply@aiesec.com', (user.email, ))




