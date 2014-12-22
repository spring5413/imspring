#-*- coding:utf-8 -*-
from piston.handler import BaseHandler
from blog.models import Article,ArticleClassify
from blog.forms import ArticleForm,ArticleClassifyForm
from piston.utils import FormValidationError
import traceback
import logging
from django.shortcuts import get_object_or_404
log = logging.getLogger('root')

class ArticleHandler(BaseHandler):
    fields = ("id","title","content","desc","source","like","ctime","utime","classify","ctype","thumbnail")
    allowed_methods = ('GET','POST','PUT','DELETE')
    model = Article
    
    def read(self,request, *args, **kwargs):
        """
        获取收藏列表
        URL:/iapi/blog/article/
        获取某一个收藏
        URL：/iapi/blog/article/(?P<id>d+)/
        参数:
        id:收藏ID
        """
        return super(ArticleHandler,self).read(request,*args,**kwargs)
    def create(self,request, *args, **kwargs):
        """
        创建收藏：
        URL:/iapi/blog/article/
        参数：
        title : 收藏标题
        content ： 收藏内容
        desc ：收藏描述（可选）
        like ： 赞
        source ： 收藏来源
        ctype : 收藏内容类型 （链接：link）  （可选） 默认是按照纯文字展现
        """
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
        URL ： /iapi/blog/article/(?P<id>d+)/
        参数：
                        所有参数均可选填
        '''
        f = ArticleForm(request.POST,request=request)
        if f.is_valid():
            try:
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
        参数：
                        收藏ID
        """
        return super(ArticleHandler,self).delete(request, *args, **kwargs)
        
class ArticleClassifyHandler(BaseHandler):
    fields = ("id","title","desc",)
    allowed_methods = ('GET','POST','PUT','DELETE')
    model = ArticleClassify
    
    def read(self,request, *args, **kwargs):
        """
        获取所有分类以及分类下的收藏
        URL:/iapi/blog/article/classify/
        """
        if 'id' in kwargs:
            classify = get_object_or_404(ArticleClassify,id=kwargs['id'])
            return classify._valueDict()
        else:
            classifys = ArticleClassify.objects.all()
            return [c._valueDictSimp() for c in classifys]
    def create(self,request, *args, **kwargs):
        """
        创建收藏分类
        URL:/iapi/blog/article/classify/
        参数：
        title : 分类名称
        desc : 分类描述
        """
        f = ArticleClassifyForm(request.POST)
        if f.is_valid():
            instance = f.save()
            return instance
        else:
            raise FormValidationError(f)