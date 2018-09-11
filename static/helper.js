function search_post(){

        var query = $('#search_bar').val();
        console.log('hello');
        url = 'list/';
        type = 'GET';
        $.ajax({
		url:url,
		type:type,
		data:{q:query},
		success:callBack,
		error:function(request, error, callBack) {
		    console.log("inside error function");
            console.log(request, error);
        }
	 });
}

function callBack(data){
debugger;
console.log(data)
//data.forEach(function(blog){
//console.log(blog['Name']);
//});
}