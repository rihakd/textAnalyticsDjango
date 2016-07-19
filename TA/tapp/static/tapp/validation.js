function validateDiscForm() {
    var x = document.forms["discForm"]["name"].value;
    if (x == null || x == "") {
        alert("Name must be filled out");
        return false;
    }
}

function validateLoginForm() {
    var x = document.forms["loginForm"]["username"].value;
    var y = document.forms["loginForm"]["password"].value;
    if (x == null || x == "" || y == null || y == "") {
        alert("Missing fields");
        return false;
    }
}

function validateSignInForm() {
    var x = document.forms["SignInForm"]["username"].value;
    var y = document.forms["SignInForm"]["password"].value;
    if (x == null || x == "" || y == null || y == "") {
        alert("Missing fields");
        return false;
    }
}