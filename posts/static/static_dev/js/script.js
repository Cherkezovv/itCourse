function basylan(al) {
    for (var i = 1; i <= 2; i++) {
        if (al == "btn" + i) {
            var sayk = document.getElementById(al);
            document.getElementById("div" + i).style.display = "block";
        } else {
            var sayk = document.getElementById("btn" + i);
            document.getElementById("div" + i).style.display = "none";
        }
    }
}


function click_q(a) {
    for (var i = 1; i <= 6; i++) {
        if (a == "q" + i) {
            var say = document.getElementById(a);
            document.getElementById("div_q" + i).style.display = "block";
        } else {
            var say = document.getElementById("q" + i);
            document.getElementById("div_q" + i).style.display = "none";
        }
    }
}