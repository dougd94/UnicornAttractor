from django.conf.urls import url, include
from .views import all_features, create_or_edit_feature, feature_detail
urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^new/$', create_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
]