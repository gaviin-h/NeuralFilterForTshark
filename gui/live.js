let btn = document.getElementById('run')
let iface = document.getElementById('interface')
let latest = document.getElementById('latest')
let output = document.getElementById('output')
let xhr = new XMLHttpRequest()

btn.addEventListener('click' () => {
    if()
})
xhr.open('GET', "{{ url_for('run') }}")
xhr.send();
var position=0

function handleNewData(){
    var messages=xhr.responseText.split('')
    messages.slice(position, -1).forEach(function(value) {
        latest.textContent = value
        var item = document.getElement('li')
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
        latest.textContnt = 'Done';
    }
}, 1000)