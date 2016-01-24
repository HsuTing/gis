from django.conf.urls import url

from twVillage import views

urlpatterns = [
    url(r'^([0-9]+)/$', views.output),
    url(r'^$', views.total),
]
