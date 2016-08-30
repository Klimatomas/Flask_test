from json import dumps
from flask import Flask
from source import Requests

app = Flask(__name__)


@app.route('/')
def s():
    gifs = s.trending()
    sounds = s.spotify(gifs)
    return dumps(s.result(sounds[0], sounds[1]))


if __name__ == '__main__':
    s = Requests()
    app.debug = True
    app.run()
