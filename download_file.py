import os

import requests
import json
from datetime import datetime
from convert_to_file import Convert
from dotenv import load_dotenv

load_dotenv()


class Download:
    def download_file_xls(self, token):
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
        file_path = os.getenv('FILE_STORAGE_REPORT_XLSX')
        convert.save_response_to_file(response_bytes, file_path)

    def download_file_pdf(self, token):
        url = "https://api.fmarket.vn/investors/assets/export"

        payload = json.dumps({
            "exportType": "PDF",
            "toDate": int(datetime.now().timestamp() * 1000)
        })
        headers = {
            'authorization': f'Bearer {token}',
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        response = requests.request("POST", url, headers=headers, data=payload)
        convert = Convert()
        response_bytes = response.content
        file_path = os.getenv('FILE_STORAGE_REPORT_PDF')
        convert.save_response_to_file(response_bytes, file_path)
