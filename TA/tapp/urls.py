from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    # sign up
    url(r'^signup/$', views.signup, name='signup'),
    # sign up process
    url(r'^signup_view/$', views.signup_view, name='signup_view'),
	# login
	url(r'^login_view/$', views.login_view, name='login_view'),
	# logout
	url(r'^logout_view/$', views.logout_view, name='logout_view'),
    # ex: /polls/
    url(r'^essay_group/$', views.essay_group, name='essay_group'),
    # filter user group 
    url(r'^(?P<filter_user_id>[0-9]+)/filter_essay_group/$', views.filter_essay_group, name='filter_essay_group'),
    # new_essay_group view
    url(r'^new_essay_group/$', views.new_essay_group, name='new_essay_group'),
    # delete essay group delete_essay_group
    url(r'^(?P<group_id>[0-9]+)/delete_essay_group/$', views.delete_essay_group, name='delete_essay_group'),
    # add essay text
    url(r'^(?P<group_id>[0-9]+)/add_essay_text/$', views.add_essay_text, name='add_essay_text'),
    # Essays view with args:  group_id 
    url(r'^(?P<group_id>[0-9]+)/essays/$', views.essays, name='essays'),
    # add_user_to_essay
    url(r'^(?P<group_id>[0-9]+)/add_user_to_essay/$', views.add_user_to_essay, name='add_user_to_essay'),
    # ex: /polls/5/
    url(r'^(?P<essay_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<essay_id>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
]