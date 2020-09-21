from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recent/$', views.recent),
    url(r'^cerita/$', views.cerita),
    url(r'^$', views.index),
]
