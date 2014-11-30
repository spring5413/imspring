# -*- coding:UTF-8 -*-
from django import forms
from blog.models import Article,ArticleClassify
import logging
log = logging.getLogger('root')

class ArticleForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request',None)
        super(ArticleForm,self).__init__(*args,**kwargs)
        if self.request and self.request.method == 'PUT':
            _fields = ['content','title']
            for f in _fields:
                self._clear_none_fields(f)
    def _clear_none_fields(self,field):
        if not self.request.data.has_key(field):
            del self.fields[field]
    class Meta:
        model = Article

class ArticleClassifyForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request',None)
        super(ArticleClassifyForm,self).__init__(*args,**kwargs)
    class Meta:
        model = ArticleClassify