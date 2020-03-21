newFunction(passWord);

function newFunction(passWord) {
    var pass = document.getElementById("strength");
    var strength = 0;
    if (password.match(/[a-zA-Z0-9]+/)) {
        strength = strength + 1;
    }
    if (password.match(/[~<>?]+/)) {
        strength = strength + 1;
    }
    if (password.match(/[!@$#&*]+/)) {
        strength = strength + 1;
    }
    if (password.length > 8) {
        strength = strength + 1;
    }
    switch (strength) {
        case 0:
            strengthBar.value = 20;
            break;
        case 1:
            strengthBar.value = 40;
            break;
        case 2:
            strengthBar.value = 60;
            break;
        case 3:
            strengthBar.value = 80;
            break;
        case 4:
            strengthBar.value = 100;
            break;
    }
}