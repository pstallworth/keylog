$(document).ready(function() {
$("#button").click(function() {
	$.post("/", {
		id: $(".text").val()
	}, function(result) {
		return $("#data").html(result.dat + " " + result.txt);
});
});
});
