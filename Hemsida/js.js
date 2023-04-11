function toggleTheme(){
    if(document.getElementById('b1').className == "danger") {
        document.getElementById('b1').classList.replace("danger", "safe");
        document.getElementById('h1').innerHTML = "SAFE";
    } else {
        document.getElementById('b1').classList.replace("safe", "danger");
        document.getElementById('h1').innerHTML = "DANGER";
    }
}