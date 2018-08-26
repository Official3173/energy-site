from django.conf.urls import url
from . import views

urlpatterns = [
    #/images/
    url(r'^$', views.index, name='index'),

    #/images/712/ - from detail view
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # this convoluted mess is a regular expression - might be worth looking up this notation

    url(r'^math/$', views.math, name='math'),

    url(r'^answer/$', views.answer, name='answer')
]

