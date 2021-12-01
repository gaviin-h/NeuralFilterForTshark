let btn = document.getElementById('btn')
let token = document.getElementById('token')
let iface = document.getElementById('interface')
let latest = document.getElementById('latest')
let output = document.getElementById('ss_elem_list')
let xhr = new XMLHttpRequest()
let post = new XMLHttpRequest()

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
var position=0
function handleNewData(){
    var messages=xhr.responseText.split('\n')
    messages.slice(position, -1).forEach(function(value) {
        latest.textContent = value
        var item = document.createElement('li')
        item.textContent=value
        output.appendChild(item);
    })
    position = messages.length-1;
}

var timer 
timer=setInterval(function() {
    handleNewData()
    if(xhr.readyState==XMLHttpRequest.DONE) {
        clearInterval(timer)
        latest.textContent = 'Stopped';
    }
}, 500)