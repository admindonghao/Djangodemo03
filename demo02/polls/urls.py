from django.conf.urls import url
from .views import *

app_name = 'polls'


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list/$', list, name='list'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^details/(\d+)/$', details, name='details'),
]
