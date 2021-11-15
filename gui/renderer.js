let input = document.querySelector('#input')
let result = document.querySelector('#result')
let btn = document.querySelector('#btn')
var{PythonShell}=require('python-shell');

function startServer(){ // no input value to this function where does it come from 
	PythonShell.run('./backend/server.py', function(err, results){
		if (err) throw err;
		// results in an array consisting of messages collected during execution
		console.log('response: ', results);
	});
}
startServer();

btn.addEventListener('click', () => {
	startServer();
});