$(function(){
	var url = window.location.href,
		article_id = parseInt(url.substr(url.indexOf("/blog/")+6));
	snow_sdk.ajax("/iapi/blog/article/"+ article_id +"/","GET","",function(data){
		var $main = $("#main"),
			$con = $main.find(".container>.content");
		$main.find("h2.title").html(data["title"]);
		$con.empty();
		if(data["ctype"] == "link"){
			$con.html($("<iframe src='"+ data["content"] +"'></iframe>"));
		}else{
			$con.html(data["content"]);
		}
	},function(){});
});