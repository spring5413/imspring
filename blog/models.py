# -*- coding:UTF-8 -*-
from django.db import models

class ArticleClassify(models.Model):
    title = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 200,blank = True)
    
    def _valueDict(self):
        return {"id":self.id,"title":self.title,"desc":self.desc,"articles":[a for a in self.articles.all()]}
    
class Article(models.Model):
    title = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 200,blank = True)
    content = models.TextField()
    like = models.IntegerField(default = 0,blank = True,null=True)
    source = models.CharField(max_length = 30,blank = True)
    ctime = models.DateTimeField(auto_now_add = True)
    utime = models.DateTimeField(auto_now = True)
    classify = models.ForeignKey(ArticleClassify,related_name="articles")
    

    
    