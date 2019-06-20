from django.conf.urls import url, include
from .views import all_features, create_feature, feature_detail, feature_upvote
urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^new/$', create_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'upvote/(?P<feature_id>[0-9]+)/$', feature_upvote, name='feature_upvote')
]