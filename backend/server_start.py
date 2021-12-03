import sys
import math
import subprocess
from flask import render_template, request 
from flask.app import Flask
from flask.typing import ResponseReturnValue
from werkzeug import datastructures
from Tshark import Tshark
from time import sleep
go_ahead=True
g_iface=''
g_t='n'
data=''
app = Flask(__name__, template_folder='../gui', static_folder='../gui')

# base route
@app.route('/')
def home():
    return render_template('index2.html')

# Runs tshark when a GET request is recieves
@app.route('/run', methods=['GET', 'POST'])
def run():
    # Generates the tshark output 
    def generate():
        global go_ahead
        from tokenizer import tokenize
        p=Tshark()
        proc=p.start(g_iface)
        while True:
            line=proc.stdout.readline()
            if not go_ahead:
                proc.terminate()
                global data
                data = proc.stdout.read().split(b'\n')
                break
            line=str(line)
            if g_t=='t':
                line=tokenize(line)
            yield str(line)+'\n'
    if request.method=='POST':
        global go_ahead
        go_ahead=True
        global g_iface
        g_iface=request.form['iface']
        global g_t
        g_t=request.form['t']
        return "recieved"
    else:
        return app.response_class(generate(), mimetype="text/plain")

@app.route('/stop', methods=['POST'])
def stop():
    global go_ahead
    go_ahead=False
    return 'stopped'

@app.route('/save', methods=['POST'])
def save():
    global data
    path=request.form['name']
    # file=open(path, 'w')
    # for line in data:
    #     file.write(line)    
    return [path]

# For testing purposes
@app.route('/stream', methods=['GET'])
def stream():
    def generate():
        for i in range(500):
            yield "{}\n".format(math.sqrt(i))
            sleep(1)
    return app.response_class(generate(), mimetype="text/plain")

# start the server
if __name__ == "__main__":
    subprocess.run(['sh', '../backend/killer.sh'])
    app.run(host='127.0.0.1', port=5001)
