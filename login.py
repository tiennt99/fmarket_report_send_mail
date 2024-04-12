import requests
import json


class Login:
    def get_token(self):
        url = "https://api.fmarket.vn/auth/login"

        payload = json.dumps({
            "email": "tiennguyenhuu1999@gmail.com",
            "password": "Tienmt@99",
            "referralCode": None
        })
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi',
            'content-type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()

        token = response.get('data').get('accessToken')
        return token
