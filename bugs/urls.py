from django.conf.urls import url, include
from .views import all_bugs, bug_detail, create_bug, bug_upvote

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'upvote/(?P<bug_id>[0-9]+)/$', bug_upvote, name='upvote'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_bug, name='new_bug'),
]