
function validateLogin() {
  var em = document.querySelector('#email').value;
  var pw = document.querySelector('#password').value;
  var email = "email";
  var password = "password";
  if ((em == email) && (pw == password)) {
    alert('You are successfully logged in');
  } else {
    alert("Login was unsuccessful, please check your email and password");
    return false;
  }
}