import requests
from requests_oauthlib import OAuth1
import json
import shutil


CLIEND_ID = "AxUbsKxiKfeh2a1voVGPCBtvT"
CLIENT_SECRET = "1OvyetB8S7pmngjHG0QLMGj7U8KEzHp468OMiNHJElFpLp3PYX"
TOKEN_KEY = "1532098049178468352-jQETxEDbXzlci3TgvsEu4f1TmkU6qv"
TOKEN_SECRET = "yng5y90Cr5JehHpsaU8MjzUNq1JSoIEwf70zmtc8ekWCg"
NASA_API = "4UeofORNY8z22PfPopgRmQzKlfmhVpalfQqZpmio"

oauth = OAuth1(CLIEND_ID,
               client_secret=CLIENT_SECRET,
               resource_owner_key=TOKEN_KEY,
               resource_owner_secret=TOKEN_SECRET,
               )


def nasa_response():
    nasa_request = requests.get(
        f"https://api.nasa.gov/planetary/apod?api_key={NASA_API}&thumbs=True&date=2022-12-14",
    )
    return nasa_request.json()


def download_image(nasa_response):

    if nasa_response["media_type"] == "image":
        image_url = nasa_response["hdurl"]
    elif nasa_response["media_type"] == "video":
        image_url = nasa_response["thumbnail_url"]

    res = requests.get(
        image_url,
        stream=True
    )
    if res.status_code == 200:
        with open(nasa_response["title"], 'wb') as f:
            shutil.copyfileobj(res.raw, f)


def check_image(nasa_response):
    image = open(nasa_response["title"], "rb")
    files = {"media": image}

    get_media_id = requests.post(
        "https://upload.twitter.com/1.1/media/upload.json",
        auth=oauth,
        files=files,
    )
    return get_media_id.json()


def twitter_response(nasa_response, image_response):
    arey = []
    arey.append(str(image_response["media_id"]))

    response = requests.post(
        "https://api.twitter.com/2/tweets",
        auth=oauth,
        json={
            "media": {"media_ids": arey},
            "text": nasa_response["title"]
        }
    )
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    nasa = nasa_response()
    download_image(nasa)
    image_data = check_image(nasa)
    twitter_response(nasa, image_data)


if __name__ == "__main__":
    main()
