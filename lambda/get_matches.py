import requests
import json
import os

def handler(event, context):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": os.environ["API_KEY"]
    }
    res = requests.get(url, headers=headers)
    return {
      "statusCode": 200,
      "body": json.dumps(res.json())
    }