from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login

# url patterns for register, profile, logout, login, index and password reset.

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^index/$', index, name='index'),
    url(r'^password-reset/', include(urls_reset)),

]
