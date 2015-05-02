__author__ = 'David'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^impressum/$', views.impressum, name='impressum'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<todo_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<todo_id>[0-9]+)/$', views.delete, name='delete'),
]