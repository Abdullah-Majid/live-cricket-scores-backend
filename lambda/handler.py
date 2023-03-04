import requests
import json
import os

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver

tracer = Tracer()
logger = Logger()
app = ApiGatewayResolver() 

@app.get("/matches")
@tracer.capture_method
def get_matches():
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

@app.get("/scorecard/<match_id>")
@tracer.capture_method
def get_scorecard(match_id):    
    url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{match_id}/scard"
    headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": os.environ["API_KEY"]
    }
    res = requests.get(url, headers=headers)
    return {
      "statusCode": 200,
      "body": json.dumps(res.json())
    }

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)