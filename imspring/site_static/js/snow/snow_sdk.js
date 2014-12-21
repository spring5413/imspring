var snow_sdk = (function(){
	var api = {},
		internal = {};
	api.ajax = function(url,type,data,callback,err_callback){
		$.ajax({
			url:url,
			type:type,
			data:data,
			statusCode:{
				200:function(data){
					callback(data);
				},
				400:function(){
					if(err_callback){err_callback();}
					else{
						alert("ajax:400");
					}
				}
			}
		});
	}
	return api;
})();