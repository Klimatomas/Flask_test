from json import dumps
from flask import Flask
from source import Requests

app = Flask(__name__)


@app.route('/')
def search():
    return dumps(search.trending())


if __name__ == '__main__':
    search = Requests()
    app.debug = True
    app.run()
