from django.conf.urls import url, include
from .views import all_features, create_or_edit_feature
urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^new/$', create_or_edit_feature, name='new_feature'),
]