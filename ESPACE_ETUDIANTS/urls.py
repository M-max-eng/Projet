from django.conf.urls import url
from  . import  views

urlpatterns = [
    url('home/',views.home),
    url('register/',views.toregister,name='reg'),
    url('forgot-password/',views.pwd,name='fpwd'),
    url('login/',views.home, name='log'),
    url('index/',views.index, name='ind'),
]