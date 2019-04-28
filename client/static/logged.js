
var saveInput = document.getElementById("saveInput");
var getInput = document.getElementById("getInput");
var saveButton = document.getElementById("saveButton");
var getButton = document.getElementById("getButton");
var getAllButton = document.getElementById("getAllButton");
var serveResponse = document.getElementById("response");
var logoutButton = document.getElementById("logoutButton");

saveButton.addEventListener("click", function() {

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': "Bearer " + localStorage.getItem('jwtoken') },
        body: JSON.stringify({ 'content': saveInput.value }),
        mode : 'cors',
    };

    if (saveInput.value === '') {
        window.alert('Ingrese una nota')
    } else {
        fetch('http://127.0.0.1:8000/notes', requestOptions)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            serveResponse.innerHTML = JSON.stringify(myJson, undefined, 2);
        })
        .catch(function(error){
            console.log(error);
        });
    }
});

getAllButton.addEventListener("click", function() {

    var bearer = "Bearer " + localStorage.getItem('jwtoken');
    const requestOptions = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'Authorization': bearer },
        mode : 'cors',
    };

    fetch('http://127.0.0.1:8000/notes', requestOptions)
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
        console.log(myJson);
        serveResponse.innerHTML = JSON.stringify(myJson, undefined, 2);
    })
    .catch(function(error){
        console.log(error);
    });
});

getButton.addEventListener("click", function() {

    var bearer = "Bearer " + localStorage.getItem('jwtoken');
    const requestOptions = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'Authorization': bearer },
        mode : 'cors',
    };

    if (getInput.value === '') {
        window.alert('Ingrese un ID para buscar')
    }
    else {
        fetch('http://127.0.0.1:8000/notes/' + getInput.value, requestOptions)
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            console.log(myJson);
            serveResponse.innerHTML = JSON.stringify(myJson, undefined, 2);
        })
        .catch(function(error){
            console.log(error);
        });
    }
});

logoutButton.addEventListener("click", function() {
    delete localStorage.jwtoken;
    window.location.replace("/");
});
