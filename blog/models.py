# -*- coding:UTF-8 -*-
from django.db import models
class ArticleModel(models.Model):
    '''
    博客
    '''
    title = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 200,blank = True)
    content = models.TextField()
    like = models.IntegerField(default = 0,blank = True,null=True)
    source = models.CharField(max_length = 30,blank = True)
    ctime = models.DateTimeField(auto_now = True)
    utime = models.DateTimeField(auto_now = True)