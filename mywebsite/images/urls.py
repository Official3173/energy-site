from django.conf.urls import url
from . import views

urlpatterns = [
    #/images/
    url(r'^$', views.index, name='index'),

    url(r'^answer/$', views.answer, name='answer'),

    url(r'^form/$', views.form),

]


