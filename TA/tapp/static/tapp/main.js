/*
$(document).ready(function(){
    $("#wrapper").on("click", "#caret", function(){
    	var range_tuple = AddSelectedText();
    	$("#start").val(range_tuple[0]);
    	$("#end").val(range_tuple[1]);
    	//AddTag();
   	});
});


function addComment() {
    alert("HELLO");
    var range_tuple = AddSelectedText();
    try {
        $("#start").val(range_tuple[0]);
        $("#end").val(range_tuple[1]);    
    } catch(err) {
        return false;
    }

    if (range_tuple[0] < 0) {
        return false;
    }
    return true;
}

function AddCommentToText(start, end) {
	var range = document.createRange();
	var startNode = document.getElementsByTagName("span")[0].firstChild;
	range.setStart(startNode, start);
	range.setEnd(startNode, end);
	range.deleteContents();
}

function AddSelectedText() {
	var fullString = document.getElementsByName("text")[0].textContent;
	if (window.getSelection) {             
		if(window.getSelection().rangeCount == 0) {
			return [-1, 0];
		}
    	var range = window.getSelection().getRangeAt(0);
    	var startPosition = fullString.search(range);
    	alert("The start position: " + startPosition);
    	var getPosition = range.toString();
    	var endPosition = parseInt(getPosition.length) + parseInt(startPosition);
    	start_position = startPosition;
    	end_position = endPosition;
    	if (start_position > 0){
    		var newNode = document.createElement("span");
    		newNode.classList.add("new");
    		range.surroundContents(newNode);
    	}
    	return [start_position, end_position];
	}
	return [-1, 0];
}
*/