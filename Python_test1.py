from flask import Flask

app = Flask(__name__)


@app.route('/asd')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def something():
    return 'lalala falala'


if __name__ == '__main__':
    app.run()
