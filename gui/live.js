let btn = document.getElementById('btn')
let btn2 = document.getElementById('btn2')
let token = document.getElementById('token')
let iface = document.getElementById('interface')
let latest = document.getElementById('latest')
let output = document.getElementById('ss_elem_list')
let btn3 = document.getElementById('btn3')
// const prompt = require('electron-prompt')
let stop = new XMLHttpRequest()
let xhr = new XMLHttpRequest()
let post = new XMLHttpRequest()
let save = new XMLHttpRequest()

btn.addEventListener('click', () => {
    post.open('POST', 'run')
    var i = iface.selectedIndex
    var t = 'n'
    if(token.checked) t = 't'
    post.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    post.send('iface=' + iface.options[i].value+'&t='+t)
    xhr.open('GET', 'run')
    xhr.send();
})
btn2.addEventListener('click', () =>{
    stop.open('POST', 'stop')
    stop.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    stop.send()
})
let directoryHandle 
let filename
btn3.addEventListener('click', ()=>{
    directoryHandle = getPath()
    directoryHandle.then(function(results){
        // prompt({
        //     title: 'file name',
        //     value: 'untitled.txt',
        //     type: 'input'
        // }).then((r) => {
        //     filename=r
        // })
        filename=prompt('file name:', 'untitled.txt')
        save.open('POST', 'save')
        save.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
        save.send('name=' + '/Users/gavin/Desktop/' + results['name'] +"/"+ filename)
    })
})

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

var timer 
timer=setInterval(function() {
    if(xhr.readyState==XMLHttpRequest.DONE) {
        clearInterval(timer)
        latest.textContent = 'Stopped';
    }    
    handleNewData()
}, 500)

async function getPath(){
    try{
        return await window.showDirectoryPicker({
            startIn: 'desktop'
        })
    } catch(e){
        console.log(e)
    }
}