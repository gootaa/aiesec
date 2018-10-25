from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .models import User
from .forms import StudentRegisterForm, CompanyRegisterForm
from .helpers import send_activation_email
from .tokens import account_activation_token


class HomePageView(TemplateView):
	template_name = 'index.html'


class StudentRegisterView(CreateView):
	model = User
	form_class = StudentRegisterForm
	template_name = 'student_register.html'

	def form_valid(self, form):
		user = form.save()
		send_activation_email(self.request, user)
		return redirect('activation-sent')


class CompanyRegisterView(CreateView):
	model = User
	form_class = CompanyRegisterForm
	template_name = 'company_register.html'

	def form_valid(self, form):
		user = form.save()
		send_activation_email(self.request, user)
		return redirect('activation-sent')


class ActivationSentView(TemplateView):
	template_name = 'activation_sent.html'


def activate_account(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		messages.success(request, 'Your account has been activated successfully.')
		return redirect('home') # can be changed later to profile
	
	else:
		return render(request, 'activation_invalid.html')


@login_required
def account_settings(request):
    """
    Displays EmailForm and PasswordChangeForm
    """
    email_form = EmailForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)

    return render(request,
                  'account-settings.html',
                  {'email_form':email_form,
                   'password_form':password_form})


@login_required
def change_email(request):
    """
    Handles EmailForm and responds to user using messages
    """
    if request.method == 'POST':
        form = EmailForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Email was updated successfully!')
        else:
            messages.error(request, 'Please enter valid data.')
    return redirect('account_settings')


@login_required
def change_password(request):
    """
    Handles PasswordChangeForm and responds to user using messages
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please enter valid data')
    return redirect('account_settings')





		

