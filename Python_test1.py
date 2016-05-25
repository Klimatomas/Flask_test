from flask import Flask
from json import dumps
import gunicorn
import requests
import grequests

app = Flask(__name__)
giphy_key = "dc6zaTOxFJmzC"


@app.route('/')
def search():
    query = "little turtles".replace(" ", "+")
    gif_array = []

    gif_request = requests.get("http://api.giphy.com/v1/gifs/search?q=" + query + "&api_key=" + giphy_key)
    gif_data = gif_request.json()
    req_set = []

    for item in gif_data["data"]:
        spotify_request = grequests.get("https://api.spotify.com/v1/search?type=track&limit=1&q=" + query)
        req_set.append(spotify_request)

    res_ary = grequests.map(req_set)

    greq_count = 0

    for item in gif_data["data"]:
        gif_music = res_ary[greq_count].json()
        gif_array.append(
            {"url": item["images"]["original"]["mp4"], "song": gif_music["tracks"]["items"][0]["preview_url"]})

        greq_count += 1

    return dumps(gif_array)


if __name__ == '__main__':
    app.debug = True
    app.run()
