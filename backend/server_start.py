import sys
import math
import subprocess
from flask import render_template, request 
from flask.app import Flask
from Tshark import Tshark
from time import sleep

app = Flask(__name__, template_folder='../gui', static_folder='../gui')

# base route
@app.route('/')
def home():
    return render_template('index2.html')

# Runs tshark when a GET request is recieves
@app.route('/run', methods=['GET', 'POST'])
def run():
    # Generates the tshark output 
    def generate(interface):
        p=Tshark()
        proc=p.start(interface)
        while True:
            line=proc.stdout.readline()
            if not line:
                break
            yield str(line)+'\n'
    if request.method=='POST':
        iface=request.form['iface']
        f=open('data.txt', 'w')
        f.write(iface)
        f.close()
        return "recieved"
    else:
        f=open('data.txt', 'r')
        iface=f.readline()
        f.close()
        return app.response_class(generate(iface), mimetype="text/plain")

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
