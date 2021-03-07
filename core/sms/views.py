import time
import requests
import hashlib
import hmac
import base64
from config.settings.base import get_secret


def api_gw_signature_v2() -> bytes:
    assess_key: str = get_secret('naver-cloud-sms-access-key-id')
    _secret_key: str = get_secret('naver-cloud-sms-secret-key')
    secret_key: bytes = bytes(_secret_key, 'UTF-8')

    method: str = 'GET'
    uri: str = f'/sms/v2/services/{get_secret("serviceId")}/messages'
    _message: str = method + '' + uri + '\n' + api_gw_timestamp() + '\n' + assess_key
    message = bytes(_message, 'UTF-8')
    sign_in_key: bytes = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    return sign_in_key


def api_gw_timestamp() -> str:
    _timestamp: int = int(time.time() * 1000)
    timestamp: str = str(_timestamp)

    return timestamp


def send_sms(phone_number, auth_number) -> requests:
    SMS_URL: str = 'https://sens.apigw.ntruss.com'

    headers: dict = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-apigw-timestamp': api_gw_timestamp(),
        'x-ncp-iam-access-key': get_secret('naver-cloud-sms-access-key-id'),
        'x-ncp-apigw-signature-v2': api_gw_signature_v2()
    }

    data: dict = {
        'type': 'SMS',
        'contentType': 'COMM',
        'countryCode': '82',
        'from': '010-4175-5261',
        'content': f'[Web] 발신 \n <개인프로젝트> 요기요 인증번호는 [{auth_number}] 입니다.\n 위 번호를 인증창에 입력하세요.',
        'messages.to': f'{phone_number}'
    }

    response = requests.post(url=SMS_URL, json=data, headers=headers)

    return response
