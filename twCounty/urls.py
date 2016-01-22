from django.conf.urls import url

from twCounty import views

urlpatterns = [
    url(r'^([0-9]+)/$', views.output),
    url(r'^$', views.total),
]
