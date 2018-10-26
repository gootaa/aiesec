from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Student, Company



GENDER_CHOICES = (
		('male', 'Male'),
		('female', 'Female'),
	)


class StudentRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    birth_date = forms.DateField(input_formats=['%Y-%m-%d',])
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.is_active = False
        user.save()
        student = Student()
        student.user = user
        student.first_name = self.cleaned_data.get('first_name')
        student.last_name = self.cleaned_data.get('last_name')
        student.birth_date = self.cleaned_data.get('birth_date')
        student.gender = self.cleaned_data.get('gender')
        student.save()
        return user


class CompanyRegisterForm(UserCreationForm):
    company_name = forms.CharField(max_length=150)
    location = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        user.is_active = False
        user.save()
        company = Company()
        company.company_name = self.cleaned_data.get('company_name')
        company.location = self.cleaned_data.get('location')


class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


