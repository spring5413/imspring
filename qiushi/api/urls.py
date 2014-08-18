# -*- coding:UTF-8 -*-
'''
Created on 2014-7-23
糗事百科
@author: spring
'''
from django.conf.urls import patterns, include, url
from utils.piston_resource import PistonResource as Resource
from qiushi.api.handlers import Qarticle

article = Resource(Qarticle)
urlpatterns = patterns('',
                       url(r'^$', article),         
)
