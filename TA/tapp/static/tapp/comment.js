function addComment() {
    var range_tuple = AddSelectedText();
    try {
        $("#start").val(range_tuple[0]);
        $("#end").val(range_tuple[1]);    
    } catch(err) {
        return false;
    }
    if (range_tuple[0] < 0 || range_tuple[0] == range_tuple[1]) {
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



function p(id, start, end){
    if(start < 0 || start == end) {
        return;
    }
    var node = document.getElementsByName("text")[0].firstChild; 
    //var fullString = node.textContent;
    var range = document.createRange();
    range.setStart(node, start);
    range.setEnd(node, end);
    var newNode = document.createElement("span");
    newNode.classList.add("new");
    newNode.classList.add(String(id));
    range.surroundContents(newNode);
    
    

}
/*
function annotate(start, end){
    alert("inside");
    break;
    if (start < 0 || start == end) {
        break;
    }

    var range = document.createRange();
    var node = document.getElementsByName("text").item(0);
    // start 
    range.setStart(node,start);    
    //end
    range.setEnd(node, end);
    range.surroundContents(newNode);
    var newNode = document.createElement("span");
    newNode.classList.add("new");
    range.surroundContents(newNode);
}
*/