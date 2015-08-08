from flask import Flask
from pony.orm import *

app = Flask(__name__)

db = Database('mysql', user='root', passwd='', db='comics', host='localhost')

from model import *

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
