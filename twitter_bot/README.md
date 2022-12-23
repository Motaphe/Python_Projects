

# NASA APOD (Astronomy Picture of the Day) Twitter Bot

This Python script uses the [NASA APOD API](https://api.nasa.gov/api.html#apod) to retrieve the "Astronomy Picture of the Day" and posts it to Twitter. It also includes functionality to handle both image and video media types.

Link to the Twitter Account - https://twitter.com/bot_motaphe

A Video Explaining the Code - https://youtu.be/OMUx9HyxnLg

## Prerequisites

- Python 3
- The following Python modules:
  - `requests`
  - `requests_oauthlib`
  - `json`
  - `shutil`

## Setup

1. Replace the placeholder values in the script with your own [Twitter API](https://developer.twitter.com/en/docs/twitter-api) and [NASA API](https://api.nasa.gov/index.html#apply-for-an-api-key) keys:
   - `CLIENT_ID`
   - `CLIENT_SECRET`
   - `TOKEN_KEY`
   - `TOKEN_SECRET`
   - `NASA_API`
2. Run the script using `python3 nasa_apod_twitter_bot.py`

## How it works

The script follows these steps:

1. Makes a GET request to the NASA APOD API to retrieve the "Astronomy Picture of the Day" data
2. Downloads the image or video thumbnail (depending on the media type)
3. Uploads the image or video to Twitter's media upload endpoint to get a media ID
4. Posts the media ID and title of the "Astronomy Picture of the Day" to Twitter's status update endpoint
