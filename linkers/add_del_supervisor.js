function rem_sup() {
  var path = require("path")
  var python = require("python-shell")

  var operation = "remove"
  var name = document.getElementById("rem_name").value
  var dept = document.getElementById("rem_dept").value
  var pos = document.getElementById("rem_pos").value
  document.getElementById("rem_name").value = "";
  document.getElementById("rem_dept").value = "";
  document.getElementById("rem_pos").value = "";

  var options = {
    scriptPath : path.join(__dirname, '/engine/'),
    args : [operation,name,dept,pos]
  }

  var weather = new python('supervisor.py', options);

}



function add_sup() {
  var path = require("path")
  var python = require("python-shell")

  var operation = "add"
  var name = document.getElementById("add_name").value
  var dept = document.getElementById("add_dept").value
  var pos = document.getElementById("add_pos").value
  document.getElementById("add_name").value = "";
  document.getElementById("add_dept").value = "";
  document.getElementById("add_pos").value = "";

  var options = {
    scriptPath : path.join(__dirname, '/engine/'),
    args : [operation,name,dept,pos]
  }

  var weather = new python('supervisor.py', options);

}
