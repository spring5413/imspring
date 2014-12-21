2014-12-21
	alter table blog_article add column ctype varchar(50) null;
	alter table blog_article add column thumbnail varchar(500) null; #这个是为了减少服务器压力，自己不存储图片文件