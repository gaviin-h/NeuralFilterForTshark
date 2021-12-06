import math
import subprocess
from flask import render_template, request 
from flask.app import Flask
from Tshark import Tshark
from time import sleep
from joblib import load
go_ahead=True
g_iface=''
g_t='n'
data=''
active_net=''

# app Instantiation
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
        ifnet=load('../backend/models/net_one.joblib')
        from tokenizer import tokenize_n
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
            t_line=tokenize_n(line)
            v=str(ifnet.predict([t_line])[0])
            if v != '1':
                v='0'
            if g_t=='t':
                yield v+str(t_line)+'\n'
            else:
                yield v+str(line)+'\n'

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
    if path[-4:]!='.txt':
        path+='.txt'
    file=open(path, 'w')
    for line in data:
        file.write(line.decode('UTF-8')+'\n') 
    file.close()   
    return 'saved'

# Recieve the data to load the net
@app.route('/load', methods=['POST'])
def load_net():
    name=request.form['name']
    # text=request.form['file_data']
    # file=open('../backend/models/'+name, 'w')
    # file.writelines(text)
    # file.close()
    global active_net
    active_net = '/Users/gavin/Desktop/CBU/'+str(name)
    return active_net

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
