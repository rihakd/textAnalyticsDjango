//globs
var active = false;

$(document).ready(function(){
	$("#wrapper").on({
	mouseover: function(){
		var clss = $(this).attr('class').split(' ')[1];
		$("." + clss).addClass("comment");
	},
	mouseout: function(){
		var clss = $(this).attr('class').split(' ')[1];
		$("." + clss).removeClass("comment");
	},
	click: function(){
		var clss = $(this).attr('class').split(' ')[1];
		if (active){
			$("." + clss).removeClass("comment_click");
		} else {
			$("." + clss).addClass("comment_click");
		}
		active = !active;
	}
}, ".comment_entry");

	$("#wrapper").on({
	mouseover: function(){
		var clss = $(this).attr('class').split(' ')[1];
		$("." + clss).addClass("comment");
	},
	mouseout: function(){
		var clss = $(this).attr('class').split(' ')[1];
		$("." + clss).removeClass("comment");
	},
	click: function(){
		var clss = $(this).attr('class').split(' ')[1];
		if (active){
			$("." + clss).removeClass("comment_click");
		} else {
			$("." + clss).addClass("comment_click");
		}
		active = !active;
	}
}, ".new");
});
