
function make_chart() {
  var path = require("path")
  var python = require("python-shell")


  var options = {
    scriptPath : path.join(__dirname, '/engine/'),
  }

  var weather = new python('create_chart.py', options);

}
