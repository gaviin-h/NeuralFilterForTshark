let btn = document.querySelector('#btn')
var {PythonShell} = require('python-shell');
let t = document.getElementById('update')
let xhr = new XMLHttpRequest

function startServer(){ // no input value to this function where does it come from 
    let options = {
        arguments: ['runserver']
    }
    PythonShell.run('../backend/server_start.py', options, function(err, results){
        if (err) console.log(err, results)
    }); 
}

async function getFile(){
    try{
        return await window.showOpenFilePicker({
            startIn: 'desktop'
        })
    } catch(e){
        console.log(e)
    }
}
// very close
let fileHandle
let fileData
let file
let text
let name
btn.addEventListener('click', () => {
    startServer()
    fileHandle = getFile()
    fileHandle.then(function(results) {
        fileData = results[0].getFile()
        fileData.then(function(result){
            file = result
            name = file.name
            file.text().then(function(r) {
                text = r
                xhr.open('POST', 'http://127.0.0.1:5001/load', false)
                xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
                xhr.onreadystatechange = function () {
                    if(xhr.readyState===XMLHttpRequest.DONE){
                        if(xhr.status===200){
                            document.body.innerHTML += "Success!"
                            window.location.assign('http://127.0.0.1:5001/')
                        }
                        else{
                            document.body.innerHTML += "Failed!"
                        }
                    }
                }
                xhr.send('name=' + name + '&file_data=' + text)
            })
        })  

    })
});