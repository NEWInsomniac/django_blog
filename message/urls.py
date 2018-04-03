from django.conf.urls import url
from .import views
app_name = 'message'

urlpatterns = [ url(r'^message$', views.my_message, name='my_message'), ]