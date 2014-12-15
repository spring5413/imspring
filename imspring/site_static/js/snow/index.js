$(function(){
	var $band = $("#band");
	setTimeout(function(){
		$band.find(".band-bg").fadeIn();
		$band.find(".band-wrap").animate({"bottom":"10%","opacity":"1"});
	},50);
});