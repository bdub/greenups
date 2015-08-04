from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
url(r'^$', views.EventIndexView.as_view(), name='event-index'),
)
