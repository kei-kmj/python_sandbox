from fastapi import FastAPI, HTTPException
import requests
from requests import RequestException

app = FastAPI()


class APIClient:
    def __init__(self, url: str):
        self.url = url

    def get_status(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise HTTPException(status_code=500, detail=str(e))

    def check_capacity(self):
        status = self.get_status()
        if status["capacity"] == "Full":
            return "No capacity"
        elif status["capacity"] == "Available":
            return "Capacity available"
        else:
            return "Status check failed"
