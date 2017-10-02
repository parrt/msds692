# get API keys: https://support.google.com/cloud/answer/6158862
# getting started: https://developers.google.com/api-client-library/python/start/get_started
# I then enabled "YouTube Data API v3"
# API doc: https://developers.google.com/youtube/v3/
# Install library: pip install --upgrade google-api-python-client

import sys
import urllib
from googleapiclient.discovery import build

DEVELOPER_KEY = sys.argv[1]
QUERY = sys.argv[2] # e.g., "cats and dogs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# code from https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Call the search.list method to retrieve results matching the specified
# query term.
search_response = youtube.search().list(
    q=QUERY,            # search terms
    part="id,snippet",  # what we want back
    maxResults=20,      # how many results we want back
    type="video"        # only tell me about videos
).execute()

# search_response is a dict
items = search_response['items']
for vid in search_response['items']:
    if vid["id"]["kind"] == "youtube#video":
        print vid['snippet']['title'], "https://www.youtube.com/watch?v="+vid['id']['videoId']
