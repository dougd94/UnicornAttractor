from django.conf.urls import url, include
from .views import logout, login, registration, user_profile, index
from . import url_reset

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/$', registration, name='registration'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
]