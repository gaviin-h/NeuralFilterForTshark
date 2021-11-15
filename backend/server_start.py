import sys
import flask
from flask.app import Flask
from flask_cors import cross_origin
        
app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
    
