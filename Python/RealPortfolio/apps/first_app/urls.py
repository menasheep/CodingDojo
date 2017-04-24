from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^projects$', views.projects),
    url(r'^about$', views.about),
    url(r'^testimonials$', views.testimonials),
]