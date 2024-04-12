import os

import requests
import json


class Login:
    def get_token(self):
        url = "https://api.fmarket.vn/auth/login"

        payload = json.dumps({
            "email": os.getenv("LOGIN_EMAIL"),
            "password": os.getenv("LOGIN_PASSWORD"),
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
