import os
import requests
import json
import time
import hmac
import hashlib

def refresh_cdn_cache(secret_id, secret_key, url_list):
    api_url = "https://cdn.tencentcloudapi.com"
    params = {
        "Action": "PurgePathCache",
        "Version": "2019-03-18",
        "Urls": url_list.split(","),
        "SecretId": secret_id,
        "Nonce": 12345,
        "Timestamp": int(time.time()),
    }
    sign_str = f"{params['Action']}{params['Version']}{params['Timestamp']}{params['Nonce']}{secret_key}"
    params["Signature"] = hmac.new(secret_key.encode('utf-8'), sign_str.encode('utf-8'), hashlib.sha1).hexdigest()
    response = requests.post(api_url, data=json.dumps(params))
    print(response.json())

if __name__ == "__main__":
    secret_id = os.getenv("TENCENT_CDN_SECRET_ID")
    secret_key = os.getenv("TENCENT_CDN_SECRET_KEY")
    url_list = os.getenv("CDN_URL_LIST")
    refresh_cdn_cache(secret_id, secret_key, url_list)