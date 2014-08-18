#-*- coding:utf-8 -*-
from piston.handler import BaseHandler
from blog.models import ArticleModel
from blog.forms import ArticleForm
from piston.utils import FormValidationError
import traceback
import logging
log = logging.getLogger('root')

class ArticleHandler(BaseHandler):
    fields = ("id","title","content","desc","source","like","ctime","utime",)
    allowed_methods = ('GET','POST','PUT','DELETE')
    model = ArticleModel
    
    def read(self,request, *args, **kwargs):
        """
        获取收藏列表
        URL:/iapi/blog/article/
        获取某一个收藏
        URL：/iapi/blog/article/(?P<id>d+)/
        """
        return super(ArticleHandler,self).read(request,*args,**kwargs)
    def create(self,request, *args, **kwargs):
        f = ArticleForm(request.POST)
        if f.is_valid():
            try:
                instance = f.save()
            except:
                log.error('article_create_error',exc_info=traceback)
        else:
            raise FormValidationError(f)
        return instance
    
    def update(self,request, *args, **kwargs):
        '''
        更新收藏
        '''
        
        f = ArticleForm(request.POST,request=request)
        if f.is_valid():
            try:
#                 request.data = f.cleaned_data.copy()
                request.data = f.request.data.copy()
                return super(ArticleHandler,self).update(request,*args,**kwargs)
            except:
                log.error('article_edit_error',exc_info=traceback)
                return rc.NOT_FOUND
        else:
            log.debug('article update error')
            raise FormValidationError(f)
        
    def delete(self,request, *args, **kwargs):
        """
        删除收藏
        URL：/iapi/blog/article/(?P<id>d+)/
        """
        return super(ArticleHandler,self).delete(request, *args, **kwargs)
        
