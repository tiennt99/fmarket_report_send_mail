import requests
import json
from datetime import datetime
from convert_to_file import Convert


class Download:
    def download_file(self, token):
        url = "https://api.fmarket.vn/investors/assets/fund-export"

        payload = json.dumps({
            "exportType": "XLS",
            "toDate": int(datetime.now().timestamp() * 1000)
        })
        headers = {
            'authorization': f'Bearer {token}',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        convert = Convert()
        response_bytes = response.content
        file_path = '/home/tiennguyen/Desktop/research/ck/tool/bao_cao.xlsx'
        convert.save_response_to_file(response_bytes, file_path)
