from django.conf.urls import url

from . import views as app_views


urlpatterns = [
	url(r'^$', app_views.HomePageView.as_view(), name='homepage'),
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
]