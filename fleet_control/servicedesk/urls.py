from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^thanks/$', thanks, name='thanks'),
    url(r'^send_mail$', contact, name='send_mail'),
]
