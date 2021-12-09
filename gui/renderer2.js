let btn = document.querySelector('#choose')
let xhr = new XMLHttpRequest

// Get the name for the file
async function getFile(){
    try{
        return await window.showOpenFilePicker({
            startIn: 'desktop'
        })
    } catch(e){
        console.log(e)
    }
}
let fileHandle
let fileData
let file
let text
let filename
// Post the net to the server
btn.addEventListener('click', () => {
    fileHandle = getFile()
    fileHandle.then(function(results) {
        fileData = results[0].getFile()
        fileData.then(function(result){
            file = result
            filename = file.name
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
                xhr.send('name=' + filename + '&file_data=' + text)
            })
        })  

    })
});