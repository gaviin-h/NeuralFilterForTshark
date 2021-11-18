let btn = document.querySelector('#btn')
var {PythonShell} = require('python-shell');
let t = document.getElementById('update')

function startServer(){ // no input value to this function where does it come from 
    let options = {
        arguments: []
    }
    PythonShell.run('../backend/server_start.py', options, function(err, results){
        if (err) console.log(err, results)
    }); 
}
startServer();

btn.addEventListener('click', () => {
	startServer();
    document.body.innerHTML += "<a type='button' href='http://127.0.0.1:5001/'>Start!</a>"
});