var login = document.getElementById("login");
var username = document.getElementById("username");
var email = document.getElementById("email");
var password = document.getElementById("password");
var register = document.getElementById("register");

register.addEventListener("click", function() {

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'username': username.value, 'password': password.value, 'email': email.value }),
        mode : 'cors',
    };

    fetch('http://127.0.0.1:8000/user/signup', requestOptions)
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
        if (myJson.status !== 'ok') {
            console.log('error en el registro');
            window.alert(JSON.stringify(myJson.errors, undefined, 2))
        }
        else {
            console.log(myJson.data);
            window.alert(JSON.stringify(myJson.data, undefined, 2));
            window.location.replace("/");
        }
    })
    .catch(function(error){
        console.log(error);
    });
});

login.addEventListener("click", function() {
    window.location.replace("/");
})