from flask import Flask
from pony.orm import *

app = Flask(__name__)

db = Database('mysql', user='db_user', passwd='db_passwd', db='comics', host='localhost')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
