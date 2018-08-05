function rem_class() {
  var path = require("path")
  var python = require("python-shell")

  var operation = "remove"
  var name = document.getElementById("rem_name").value
  document.getElementById("rem_name").value = "";


  var options = {
    scriptPath : path.join(__dirname, '/engine/'),
    args : [operation,name]
  }

  var weather = new python('classroom.py', options);

}



function add_class() {
  var path = require("path")
  var python = require("python-shell")

  var operation = "add"
  var name = document.getElementById("add_name").value
  var cap = document.getElementById("add_cap").value
  document.getElementById("add_name").value = "";
  document.getElementById("add_cap").value = "";

  var options = {
    scriptPath : path.join(__dirname, '/engine/'),
    args : [operation,name,cap]
  }

  var weather = new python('classroom.py', options);

}
