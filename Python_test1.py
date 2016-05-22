from flask import Flask
import gunicorn
import urllib2
import json

# key = "dc6zaTOxFJmzC"


# http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC
app = Flask(__name__)
key = "dc6zaTOxFJmzC"
json_dict = {}


@app.route('/asd')
def hello_world():
    return 'Hello World!'


@app.route('/')
def search():
    query = "cute tortoise"
    real_query = ""
    for i in query:
        if i == " ":
            real_query += "+"
        else:
            real_query += i

    json_object = urllib2.urlopen("http://api.giphy.com/v1/gifs/search?q=" + real_query + "&api_key=" + key)
    data = json.load(json_object)

    #
    # for item in data["data"]:
    #     if not "url" in json_dict:
    #         json_dict["url"] = [item["url"]]
    #     else:
    #         json_dict["url"].append(item["url"])


   # return json_dict


if __name__ == '__main__':
    app.run()
