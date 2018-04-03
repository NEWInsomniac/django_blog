from django.conf.urls import url
from .import views
app_name = 'users'

urlpatterns = [ url(r'^show$', views.know_me, name='know_me'), ]