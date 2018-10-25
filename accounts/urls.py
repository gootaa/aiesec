from django.conf.urls import url

from . import views as app_views
from django.contrib.auth import views as auth_views



urlpatterns = [
	# Homepage
	url(r'^$',
	app_views.HomePageView.as_view(),
	name='homepage'),
	# Registration and Activation URLS
	url(r'^register/$',
		app_views.StudentRegisterView.as_view(),
		name='student-register'),
	url(r'^company-register/$',
		app_views.CompanyRegisterView.as_view(),
		name='company-register'),
	url(r'^activation-sent/$',
		app_views.ActivationSentView.as_view(),
		name='activation-sent'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        app_views.activate_account,
		name='activate-account'),
	# Login/Logout URLS
	url(r'^login/$',
		auth_views.login,
		name='login'),
    url(r'^logout/$',
		auth_views.logout,
		{'next_page': '/'},
		name='logout'),
	# Password Reset URLS
	url(r'^password_reset/$',
		auth_views.password_reset,
		name='password_reset'),
    url(r'^password_reset/done/$',
		auth_views.password_reset_done,
		name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
		name='password_reset_confirm'),
    url(r'^reset/done/$',
		auth_views.password_reset_complete,
		name='password_reset_complete'),
	# Account Settings URLS
    url(r'^account-settings/$',
        app_views.account_settings,
        name='account_settings'),
    url(r'^change-email/$',
        app_views.change_email,
        name='change_email'),
    url(r'^change-password/$',
        app_views.change_password,
        name='change_password'),
]