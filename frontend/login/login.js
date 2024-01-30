document.addEventListener('DOMContentLoaded', () => {
    login()
})

function login() {
    document.getElementById('loginButton').addEventListener('click', function() {
        var email = document.getElementById('email').value; 
        var password = document.getElementById('password').value; 

        if (email !== '' && password !== '') {
            window.location.href = '../home/index.html';
        }
    })
}