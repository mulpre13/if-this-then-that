import requests
from requests.auth import HTTPBasicAuth


class Caldav:
    def __init__(self, server_url: str, id: str, password: str):
        self.server_url = server_url
        self.id = id
        self.password = password

    def get(self):
        return requests.get(self.server_url, auth=HTTPBasicAuth(self.id, self.password))
