# -*- coding:UTF-8 -*-
'''
Created on 2014-8-17
博客
@author: spring
'''
from django.conf.urls import patterns, include, url
from utils.piston_resource import PistonResource as Resource
from blog.api.handlers import ArticleHandler,ArticleClassifyHandler

article_handler = Resource(ArticleHandler)
article_classify_handler = Resource(ArticleClassifyHandler)

urlpatterns = patterns('',
                       url(r'^article/$', article_handler),
                       url(r'^article/(?P<id>\d+)/$', article_handler),
                       url(r'^article/classify/$', article_classify_handler),
                       url(r'^article/classify/(?P<id>\d+)/$', article_classify_handler),
)
