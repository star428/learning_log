"""定义learninglogs的url模式"""

from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name='index'),]
