let btn = document.getElementById('btn')
let btn2 = document.getElementById('btn2')
let token = document.getElementById('token')
let iface = document.getElementById('interface')
let latest = document.getElementById('latest')
let output = document.getElementById('ss_elem_list')
let btn3 = document.getElementById('btn3')
let box = document.getElementById('listbox')
let backbtn = document.getElementById('backbtn')

let stop = new XMLHttpRequest()
let xhr = new XMLHttpRequest()
let post = new XMLHttpRequest()
let save = new XMLHttpRequest()
let back = new XMLHttpRequest()

// Get data from the server
let saved=false
let saveStop
btn.addEventListener('click', () => {
    // if(output.hasChildNodes && !saved){
    //     // prompt user about the unsaved data
    //     saveStop = window.open("not_saved","Ratting","width=550,height=170,left=150,top=200,toolbar=0,status=0,")
    //     window.addEventListener('message', function(r){
    //         if(r.data === 'goback'){
    //             return null
    //         }else{
    //             continue
    //         }
    //     }, true)
    // }
    post.open('POST', 'run')
    var i = iface.selectedIndex
    var t = 'n'
    if(token.checked) t = 't'
    post.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    post.send('iface=' + iface.options[i].value+'&t='+t)
    xhr.open('GET', 'run')
    xhr.send();
})

// Stop the listener
btn2.addEventListener('click', () =>{
    stop.open('POST', 'stop')
    stop.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    stop.send()
})

// Save the current data set
let directoryHandle 
let childHandle
let filename
btn3.addEventListener('click', ()=>{
    directoryHandle = getPath()
    directoryHandle.then(function(results){
        childHandle = window.open("prompt","Ratting","width=550,height=170,left=150,top=200,toolbar=0,status=0,")
        window.addEventListener('message', function(r){
            filename=r.data
            save.open('POST', 'save')
            save.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
            save.send('name=' + '/Users/gavin/Desktop/' + results['name'] +"/"+ filename)
        }, true)
    })
    saved=true
})

// Go back to the front page
backbtn.addEventListener('click', () => {
    window.location.assign('http://127.0.0.1:5001/front')
})

// Handle new data as it comes in
var position=0
function handleNewData(){
    var messages=xhr.responseText.split('\n')
    messages.slice(position, -1).forEach(function(value) {
        let anom=false
        if(value[0]==='0'){anom=true}
        value=String(value).substring(3,value.length-2)
        latest.textContent = value
        var item = document.createElement('li')
        item.textContent=value
        item.className=String(anom)
        output.appendChild(item);
    })
    position = messages.length-1;
}

// Listen for updates 
var loading = false
var timer 
timer=setInterval(function() {
    if(xhr.readyState===XMLHttpRequest.DONE) {
        clearInterval(timer)
        latest.textContent = 'Stopped';
    } 
    // else if(xhr.readyState===3 && loading){
    //     loading = false
    //     loader = document.getElementById('loader')
    //     loader.remove()
    // }
    // else if(xhr.readyState===2 && !loading){
    //     loading=true
    //     var loader = document.createElement('div')
    //     loader.className = 'loader'
    //     loader.id = 'loader'
    //     box.appendChild(loader)
    // }   
    handleNewData()
}, 500)

// Get the directory to save in
async function getPath(){
    try{
        return await window.showDirectoryPicker({
            startIn: 'desktop'
        })
    } catch(e){
        console.log(e)
    }
}