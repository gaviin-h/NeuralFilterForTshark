import sys
import math
import subprocess
from flask import render_template, request 
from flask.app import Flask
from Tshark import Tshark
from time import sleep

app = Flask(__name__, template_folder='../gui', static_folder='../gui')

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/run', methods=['GET'])
def run():
    def generate():
        p=Tshark()
        proc=p.start('en0')
        while True:
            line=proc.stdout.readline()
            if not line:
                break
            yield str(line)
    return app.response_class(generate(), mimetype="text/plain")

@app.route('/stream', methods=['GET'])
def stream():
    def generate():
        for i in range(500):
            yield "{}\n".format(math.sqrt(i))
            sleep(1)
    return app.response_class(generate(), mimetype="text/plain")

if __name__ == "__main__":
    subprocess.run(['sh', '../backend/killer.sh'])
    app.run(host='127.0.0.1', port=5001)
