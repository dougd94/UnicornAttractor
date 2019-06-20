from django.conf.urls import url, include
from .views import logout, login, registration, user_profile, index, Get_Data
# delete
from . import url_reset

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^chart/data/$', Get_Data, name="Get_Data"),
    url(r'^register/$', registration, name='registration'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
]