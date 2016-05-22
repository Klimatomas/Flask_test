from flask import Flask, jsonify
import gunicorn
import requests
from json import dumps

# import grequests

app = Flask(__name__)
key = "dc6zaTOxFJmzC"


@app.route('/')
def search():
    query = "kittens".replace(" ", "+")
    gif_array = []
    gif_request = requests.get("http://api.giphy.com/v1/gifs/search?q=" + query + "&api_key=" + key)
    gif_data = gif_request.json()

    for item in gif_data["data"]:
        spotify_request = requests.get("https://api.spotify.com/v1/search?type=track&limit=1&q=" + query)
        gif_music = spotify_request.json()

        gif_array.append(
            {"url": item["images"]["original"]["mp4"], "song": gif_music["tracks"]["items"][0]["preview_url"]})

    return dumps(gif_array)


if __name__ == '__main__':
    app.debug = True
    app.run()
