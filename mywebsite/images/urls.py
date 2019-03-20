from django.conf.urls import url
from . import views

urlpatterns = [
    #/images/
    
    url(r'^$', views.index, name='index'),

    url(r'^finalimage/$', views.final_image, name='final_image'),

    url(r'^form/$', views.form),

    url(r'^sign_in/$', views.sign_in),

    url(r'^sign_up/$', views.sign_up),

]


