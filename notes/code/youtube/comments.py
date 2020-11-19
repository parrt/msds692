import sys
import urllib
from googleapiclient.discovery import build

DEVELOPER_KEY = sys.argv[1]
QUERY = sys.argv[2] # e.g., "cats and dogs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def videoIDs(query):
#    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=query,            # search terms
        part="id,snippet",  # what we want back
        maxResults=10,      # how many results we want back
        type="video"        # only tell me about videos
    ).execute()

    ids = [vid['id']['videoId'] for vid in search_response['items']]
    return ids

def comments(query):
    ids = videoIDs(query)
    comments = {} # map video ID to list of comment strings
    for id in ids:
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=id,
            textFormat="plainText"
        ).execute()

        comments[id] = []
        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]
            author = comment["snippet"]["authorDisplayName"]
            text = comment["snippet"]["textDisplay"]
            comments[id].append("Comment by %s: %s" % (author, text))
    return comments

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
allcomments = comments(QUERY)
for vid in allcomments.keys(): # just 5 videos
    comments = allcomments[vid]
    print("Video "+vid)
    print("\t",)
    print('\n\t'.join(comments))
