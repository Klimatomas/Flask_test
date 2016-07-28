import grequests
import requests
from json import dumps
from flask import Flask


app = Flask(__name__)
giphy_key = "api_key=dc6zaTOxFJmzC"


def slug_interpreter(slug, ident):
    slug = slug.replace(ident, "").strip("-")

    if len(slug) <= 1:
        return None
    else:
        if "-" not in slug:
            return slug
        else:
            return ' OR '.join(str.split(slug, "-")[:2])


@app.route('/')
def search():
    gif_array = []
    req_set = []
    ary = []
    gif_request = requests.get("http://api.giphy.com/v1/gifs/trending?" + giphy_key)
    gif_data = gif_request.json()

    for item in gif_data["data"]:
        query = slug_interpreter(str(item["slug"]), str(item["id"]))
        if query:
            ary.append({"slug": item["slug"], "url": item["images"]["original"]["mp4"]})
            spotify_request = grequests.get(
                "https://api.spotify.com/v1/search?type=track&limit=1&q=" + query)
            req_set.append(spotify_request)

    res_ary = grequests.map(req_set)

    greq_count = 0

    for item in ary:
        gif_music = res_ary[
            greq_count].json() 
        if gif_music["tracks"]["total"] == 0:
            continue
        else:
            gif_array.append(
                {"url": item["url"], "song": gif_music["tracks"]["items"][0]["preview_url"]})
        greq_count += 1

    return dumps(gif_array)


if __name__ == '__main__':
    app.debug = True
    app.run()
