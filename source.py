import grequests
import requests


class Requests(object):
    def __init__(self):
        self.giphy_key = "api_key=dc6zaTOxFJmzC"
        self.spotify_url = "https://api.spotify.com/v1/search?type=track&limit=1&q="

    def trending(self):
        trending_url = "http://api.giphy.com/v1/gifs/trending?"
        gif_data = requests.get(trending_url + self.giphy_key).json()
        return self.spotify(gif_data)

    def spotify(self, gif_data):
        req_set = []
        ary = []
        for item in gif_data["data"]:
            query = self.slug_interpreter(str(item["slug"]), str(item["id"]))
            if query:
                ary.append({"slug": item["slug"], "url": item["images"]["original"]["mp4"]})
                req_set.append(grequests.get(self.spotify_url + query))

        res_ary = grequests.map(req_set)
        return self.result(res_ary, ary)

    @staticmethod
    def result(res_ary, ary):
        gif_array = []
        for i, item in enumerate(ary):
            gif_music = res_ary[i].json()
            if gif_music["tracks"]["total"] == 0:
                continue
            else:
                gif_array.append(
                    {"url": item["url"], "song": gif_music["tracks"]["items"][0]["preview_url"]})

        return gif_array

    @staticmethod
    def slug_interpreter(slug, ident):
        slug = slug.replace(ident, "").strip("-")

        if len(slug) <= 1:
            return None
        else:
            if "-" not in slug:
                return slug
            else:
                return ' OR '.join(str.split(slug, "-")[:2])
