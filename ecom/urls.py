from django.conf.urls import patterns, url

from ecom import views

urlpatterns = patterns('',
  url(r'^$', views.ecom_list, name='ecom_list'),
  url(r'^new$', views.ecom_create, name='ecom_create'),
  url(r'^edit/(?P<pk>\d+)$', views.ecom_update, name='ecom_update'),
  url(r'^delete/(?P<pk>\d+)$', views.ecom_delete, name='ecom_delete'),
)