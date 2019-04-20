from django.conf.urls import url
from .views import *

app_name = 'booktest'


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list/$', list, name='list'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^deletebook/(\d+)$', deletebook, name='deletebook'),
    url(r'^deletehero/(\d+)$', deletehero, name='deletehero'),
    url(r'^addbook/$', addbook, name='addbook'),
    url(r'^addbooks/$', addbooks, name='addbooks'),
    url(r'^update/(\d+)/$', update, name='update'),
    url(r'^updates/(\d+)/$', updates, name='updates'),
    url(r'^create/(\d+)/$', create, name='create'),
    url(r'^creates/(\d+)/$', creates, name='creates'),
]
