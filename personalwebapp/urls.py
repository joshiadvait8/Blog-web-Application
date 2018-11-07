from django.conf.urls import url,include
from . import views

urlpatterns = [
url(r'^home/$', views.index, name='index'),
url(r'^contact/$',views.contact, name='contact'),]
