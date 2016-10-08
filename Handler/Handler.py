import requests

class Request():
    def __init__(self):
        self.request = requests.get('http://pii-chan.tk')
        
    def getResponseStatus(self):
        self.response = self.request.status_code
        return self.response
    