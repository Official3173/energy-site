from django.conf.urls import url
from . import views

urlpatterns = [
    #/images/
    # all these urls are added after localhost:8000
    url(r'^$', views.index, name='index'),

    url(r'^answer/$', views.answer, name='answer'),

    url(r'^form/$', views.form),

    url(r'^sign_in/$', views.sign_in),

    url(r'^sign_up/$', views.sign_up),

]


