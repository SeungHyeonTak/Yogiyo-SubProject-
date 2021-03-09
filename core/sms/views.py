import json
import time
import requests
import hashlib
import hmac
import base64
from config.settings.base import get_secret


def send_sms():
    sid = get_secret("serviceId")
    sms_uri = f'/sms/v2/services/{sid}/messages'
    sms_url = f'https://sens.apigw.ntruss.com{sms_uri}'

    acc_key_id = get_secret("ncloud-sms-access-key-id")
    acc_sec_key = b'get_secret("ncloud-sms-access-secret-key")'

    stime = int(float(time.time()) * 1000)

    hash_str = f"POST {sms_uri}\n{stime}\n{acc_key_id}"

    digest = hmac.new(acc_sec_key, msg=hash_str.encode('utf-8'), digestmod=hashlib.sha256).digest()
    d_hash = base64.b64encode(digest).decode()

    from_no = "01041755261"
    to_no = "01041755261"
    message = "SMS TEST"

    msg_data = {
        'type': 'SMS',
        'countryCode': '82',
        'from': f'{from_no}',
        'contentType': 'COMM',
        'content': f'{message}',
        'message': [{
            'to': f'{to_no}'
        }]
    }

    response = requests.post(
        sms_url, data=json.dumps(msg_data),
        headers={
            "Content=Type": "application/json; charset=utf-8",
            "x-ncp-apigw-timestamp": str(stime),
            "s-ncp-iam-access-key": acc_key_id,
            "x-ncp-apigw-signature-v2": d_hash
        }
    )

    print(response)
    print(response.text)
