$(function(){
	var $container = $("#main .container");
	snow_sdk.ajax("/iapi/blog/article/classify/","GET","",function(data){ // 初始化，显示分类
		var tmpl_articles_list = _.template($('#tmpl-articles-list').html(),{});
		$container.find("ul.siderbar").html(tmpl_articles_list({"lists":data}));
		if(data.length){
			$container.find("ul.siderbar li:eq(0)").trigger("click");
		}
	});
	$container.find("ul.siderbar").on("click","li",function(){ // 注册事件，展开该分类下的收藏
		var self = $(this),
			classify_id = self.attr("classify_id");
		self.addClass("active").siblings("li").removeClass("active");
		if(!classify_id){return;}
		snow_sdk.ajax("/iapi/blog/article/classify/"+ classify_id +"/","GET","",function(data){
			var $ul = $container.find("ul.articles");
			if(data["articles"].length){
				var tmpl_articles = _.template($('#tmpl-articles').html(),{});
				$ul.html(tmpl_articles({"articles":data["articles"]}));
			}else{
				$ul.html("<p>暂无内容</p>");
			}
		});
	})
});