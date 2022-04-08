import requests

class UserClient:
    @staticmethod
    def get_user(token):
        headers = {
            'Authorization': token
        }
        try:
            response = requests.request(method="GET", url='http://cbooks_user-service:5001/api/user', headers=headers)
        except requests.exceptions.ConnectionError:
            return 'network error'
        
        if response.status_code == 401 or response.status_code == 404:
            return False
        user = response.json()
        return user

