# -*- coding:UTF-8 -*-
'''
Created on 2014-6-23

@author: spring
'''
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from utils.piston_resource import PistonResource as Resource

urlpatterns = patterns('',
	url(r'^$',TemplateView.as_view(template_name="articles.html") , name="articles"),
	url(r'^(?P<article_id>\d+)/$',TemplateView.as_view(template_name="article_info.html") , name="article_info")   
)
