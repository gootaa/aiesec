from django.conf.urls import url

from . import views as app_views


urlpatterns = [
	url(r'^$', app_views.HomePageView.as_view(), name='homepage'),
]