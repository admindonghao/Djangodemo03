from django.conf.urls import url
from .views import *

app_name = 'polls'


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list/$', list, name='list'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^details/(\d+)/$', details, name='details'),
    url(r'^deleteiss/(\d+)/$', deleteiss, name='deleteiss'),
    url(r'^deletec/(\d+)/$', deletec, name='deletec'),
    url(r'^updeta/(\d+)/$', update, name='update'),
    url(r'^updetas/(\d+)/$', updates, name='updates'),
    url(r'^addw/$', addw, name='addw'),
    url(r'^addws/$', addws, name='addws'),
    url(r'^createch/(\d+)/$', createch, name='createch'),
    url(r'^createchs/(\d+)/$', createchs, name='createchs'),
    url(r'^result/$', result, name='result'),
]
