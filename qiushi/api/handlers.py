#-*- coding:utf-8 -*-
from piston.handler import BaseHandler
import urllib,urllib2  
import re
import logging
log = logging.getLogger('root')

class Qarticle(BaseHandler):
    allowed_methods = ("GET",)
    def read(self,request, *args, **kwargs):
        headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
#         log.debug("linking...")
        url = "http://www.qiushibaike.com/8hr/page/2?s=4687082"
        req = urllib2.Request(url,headers=headers) #伪装成浏览器访问（修改一下headers）
        content = urllib2.urlopen(req)
        content = content.read()
#         log.debug("download")
        content = content.decode("utf-8")
        #myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',content,re.S)
        sreg = '<div.*?class="content".*?title="(.*?)">(.*?)</div>'
        sreg += '.*?<div.*?class="stats clearfix">.*?<i.*? class="number">(.*?)</i>'
        sreg += '.*?<i.*?class="number">(.*?)</i>'
        myItems = re.findall(sreg,content,re.S)
        items = [] 
        for item in myItems:
            dict = {}
            dict["time"] = item[0].replace("\n","")
            dict["content"] = item[1].replace("\n","")
            dict["vote"] = item[2].replace("\n","")
            dict["comment"] = item[3].replace("\n","")
            items.append(dict)
        return items