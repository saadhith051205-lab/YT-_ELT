import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
key = os.getenv("key")

def get_playlist_id():
    try:
        
        r = requests.get(
            "https://youtube.googleapis.com/youtube/v3/channels",
            params={
                "part": "contentDetails",
                "forHandle": "MrBeast",
                "key": key
            },
            timeout=15
        )

        data=r.json()
        r.raise_for_status()

        #print(json.dumps(data, indent=4))
        channel_items=data['items'][0]
        channel_playlistId=channel_items['contentDetails']['relatedPlaylists']['uploads']
        #print(channel_playlists)
        print(channel_playlistId)
    except requests.exceptions.RequestException as e:
        raise e
if __name__ == "__main__":
    get_playlist_id()

