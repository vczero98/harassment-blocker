window.onload = function hideHarassment() {
	console.log("hi")
	var slides = document.getElementsByClassName("UFICommentBody");
	console.log(slides.length);
	var counter = 0;
	var messages = [];
	for(var i = 0; i < slides.length; i++) {
		messages.push($(slides.item(i).childNodes[0]).text());
		messages[i] = messages[i].replace(/\,/g,"")
	}

	console.log(JSON.stringify(messages))

	$.getJSON("http://localhost:5000/analyse_text/", {text:JSON.stringify(messages)}, function(data) {
		var replies = data.replies;
			console.log(slides.length)
			for(var i = slides.length - 1; i >= 0; i--)  {
				console.log(data.replies[i])
				if (replies[i]) {
					console.log($(slides.item(i).childNodes[0]));
					$(slides.item(i).childNodes[0]).text("hello");
					var parentDiv = $($(slides.item(i).childNodes[0])).parent().parent().parent().parent().parent().parent().parent().parent().parent().parent();
					parentDiv.css("background", "#FFCCCC");
					parentDiv.css("padding", "5px");
					parentDiv.html("<img src='http://localhost:5000/static/icon.png'> <div style='font-style:italic; display:inline-block;'> Comment hidden by HarassmentBlocker</div>");
				}
			}
	});
}
