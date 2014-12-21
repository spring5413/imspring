# -*- coding:UTF-8 -*-
from django.db import models

class ArticleClassify(models.Model):
    title = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 200,blank = True)
    
    def _valueDict(self):
        return {"id":self.id,"title":self.title,"desc":self.desc,"articles":[a._valueSimp() for a in self.articles.all()]}
    
class Article(models.Model):
    title = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 200,blank = True)
    content = models.TextField()
    like = models.IntegerField(default = 0,blank = True,null=True)
    source = models.CharField(max_length = 30,blank = True)
    ctime = models.DateTimeField(auto_now_add = True)
    utime = models.DateTimeField(auto_now = True)
    classify = models.ForeignKey(ArticleClassify,related_name="articles")
    ctype = models.CharField(max_length = 50,blank = True)
    thumbnail = models.CharField(max_length = 500,blank = True)

    def _valueSimp(self):
        return {"id":self.id,"title":self.title,"ctime":self.ctime,"ctype":self.ctype,"thumbnail":self.thumbnail,"desc":self.desc}
    

    
    