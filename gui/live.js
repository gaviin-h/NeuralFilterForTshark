let btn = document.getElementById('btn')
let iface = document.getElementById('interface')
let latest = document.getElementById('latest')
let output = document.getElementById('output')
let xhr = new XMLHttpRequest()

btn.addEventListener('click', () => {
    alert("js working")
})

xhr.open('GET', 'stream', true)
xhr.send();

var position=0
function handleNewData(){
    var messages=xhr.responseText.split('\n')
    messages.slice(position, -1).forEach(function(value) {
        latest.textContent = value
        var item = document.createElement('li')
        item.textContent=value
        output.appendChild(item);
    })
    position = messages.length-1
}

var timer
timer=setInterval(function() {
    handleNewData()
    if(xhr.readyState==XMLHttpRequest.DONE) {
        clearInterval(timer)
        latest.textContent = 'Done';
    }
}, 500)