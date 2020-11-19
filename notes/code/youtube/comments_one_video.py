import sys
from googleapiclient.discovery import build

DEVELOPER_KEY = sys.argv[1]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

video_id = "gU_gYzwTbYQ"  # bonkers the cat

# code from https://developers.google.com/youtube/v3/docs/comments/list
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText"
  ).execute()

for item in results["items"]:
    comment = item["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print("Comment by %s: %s" % (author, text))
