from flask import Flask

from flask_cors import CORS

from numpy import genfromtxt

app = Flask(__name__)
CORS(app)



@app("")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)