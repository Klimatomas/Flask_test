from flask import Flask
import urllib2

# key = "dc6zaTOxFJmzC"


# http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC
app = Flask(__name__)
key = "dc6zaTOxFJmzC"


@app.route('/asd')
def hello_world():
    return 'Hello World!'


@app.route('/')
def search():
    query = raw_input("Insert search query: ")
    real_query = ""
    for i in query:
        if i == " ":
            real_query += "+"
        else:
            real_query += i

    response = urllib2.urlopen("http://api.giphy.com/v1/gifs/search?q=" + real_query + "&api_key=" + key)
    result = response.read()
    print result

    return "Search results for: " + query + result


if __name__ == '__main__':
    app.run()
