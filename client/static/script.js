
var login = document.getElementById("login");
var username = document.getElementById("username");
var password = document.getElementById("password");
var register = document.getElementById("register");

login.addEventListener("click", function() {

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'username': username.value, 'password': password.value }),
        mode : 'cors',
    };

    fetch('http://127.0.0.1:8000/user/login', requestOptions)
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
        if (myJson.jwtoken) {
            localStorage.setItem('jwtoken', myJson.jwtoken);
            window.location.replace("/logged");
        }
        else {
            window.alert(myJson.errors)
        }
    })
    .catch(function(error){
        console.log(error);
    });
});

register.addEventListener("click", function() {
    window.location.replace("/register");
})


