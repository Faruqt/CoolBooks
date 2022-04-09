import requests
import os
from dotenv import load_dotenv 

load_dotenv()

service_url = os.environ['USER-SERVICE']
class UserClient:
    @staticmethod
    def get_user(token):
        headers = {
            'Authorization': token
        }
        try:
            response = requests.request(method="GET", url=service_url, headers=headers)
        except requests.exceptions.ConnectionError:
            return 'network error'
        
        if response.status_code == 401 or response.status_code == 404:
            return False
        user = response.json()
        return user

