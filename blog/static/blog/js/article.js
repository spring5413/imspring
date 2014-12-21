$(function(){
	snow_sdk.ajax("/iapi/blog/article/classify/","GET","",function(data){
		var tmpl_articles = _.template($('#tmpl-articles').html(),{});
		$("#main .container").html(tmpl_articles({"articles":data[0]["articles"]}));
	});
});