from django.contrib.auth.models import AbstractUser
from django.db import models

from .langs import langs
from .countries import countries


class User(AbstractUser):

	USER_TYPE_CHOICES = (
		(1, 'student'),
		(2, 'company'),
	)

	first_name = None
	last_name = None
	email = models.EmailField(('email address'), blank=False)
	user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
	image = models.ImageField(upload_to='account_imgs/', blank=True)


class Student(models.Model):

	GENDER_CHOICES = (
		('male', 'Male'),
		('female', 'Female'),
	)

	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	birth_date = models.DateField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	resume = models.FileField(upload_to='resumes/', blank=True)


class Company(models.Model):
	user = models.OneToOneField(User)
	company_name = models.CharField(max_length=150)
	location = models.CharField(max_length=150)
	description = models.TextField(blank=True)


class Language(models.Model):

	LANGUAGE_CHOICES = langs
	LEVEL_CHOICES = (
		(1, 'limited'),
		(2, 'conversational'),
		(3, 'fluent'),
		(4, 'native'),
	)

	student = models.ForeignKey(Student, related_name='languages')
	language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
	level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)


class Degree(models.Model):

	LEVEL_CHOICES = (
		(1, 'high school'),
		(2, 'associate degree'),
		(3, 'bachelor'),
		(4, 'masters'),
		(5, 'doctorate'),
		(6, 'other'),
	)

	student = models.ForeignKey(Student, related_name='degrees')
	institute_name = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField()
	background = models.CharField(max_length=150)
	level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)


class WorkExperience(models.Model):

	student = models.ForeignKey(Student, related_name='experiences')
	job_title = models.CharField(max_length=100)
	company_name = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField()
	current_role = models.BooleanField()
	description = models.TextField()


class Nationality(models.Model):

	NATIONALITY_CHOICES = countries

	student = models.ForeignKey(Student, related_name='nationalities')
	nationality = models.CharField(max_length=10, choices=countries)







