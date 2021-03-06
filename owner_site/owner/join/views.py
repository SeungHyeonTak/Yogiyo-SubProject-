import datetime
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from app.models import ApplicationForm
from core.sms.models import AuthSms
from core.sms.views import *


def process(request) -> HttpResponse:
    context: dict = {}
    return render(request, 'join/process.html', context)


@csrf_exempt
def online_entry(request) -> HttpResponse:
    context: dict = {}
    phone_first_numbers: list = ['010', '011', '016', '017', '018', '019', '0130']

    context.update({
        'phone_first_numbers': phone_first_numbers
    })

    return render(request, 'join/request.html', context)


@csrf_exempt
def ajax_license_validate(request) -> HttpResponse:
    license_number: str = request.POST.get('company_number')
    return_type: str = 'application/json'
    return_status_code: int = 200
    response: dict = {}

    license_number_len: int = len(license_number.replace("-", ""))
    if license_number_len != 10:
        response.update({
            'success': False,
            'error': {
                'code': 'invalid_company_number'
            }
        })
    else:
        af: ApplicationForm = ApplicationForm.objects.filter(license_number=license_number)
        if af:
            if af.filter(is_check=True, final_confirmation=False):
                response.update({
                    'success': False,
                    'error': {
                        'code': 'already_request'
                    }
                })
            else:
                response.update({
                    'success': False,
                    'error': {
                        'code': 'is_duplicate'
                    }
                })
        else:
            response.update({'success': True})

    return HttpResponse(json.dumps(response), return_type, return_status_code)


@csrf_exempt
def ajax_phone_sms_authentication(request) -> HttpResponse:
    return_type: str = 'application/json'
    return_status_code: int = 200
    response: dict = {}

    if request.method == 'POST':
        phone_number: str = request.POST.get('mobile_phone_number')
        try:
            # 이미 인증됨
            subscriber_search: AuthSms = AuthSms.objects.get(phone_number=phone_number)
            # auth_number: int = subscriber_search.auth_number
            send_sms()
            response.update({})
        except AuthSms.DoesNotExist:
            # 첫 인증
            auth_sms: AuthSms = AuthSms(
                phone_number=phone_number
            )
            auth_sms.save()
            auth_number: int = auth_sms.auth_number
            send_sms()
            response.update({'auth_number': auth_number})
        except KeyError:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(json.dumps(response), return_type, return_status_code)


@csrf_exempt
def ajax_sms_code_validate(request) -> HttpResponse:
    return_type: str = 'application/json'
    return_status_code: int = 200
    response: dict = {}
    code: str = request.POST.get('code')
    phone_number: str = request.POST.get('phone_number')

    now = timezone.localtime(timezone.now())
    min_3 = now + datetime.timedelta(minutes=3)

    try:
        auth_sms = AuthSms.objects.get(phone_number=phone_number, auth_number=code)
        if auth_sms and (now > min_3):
            response.update({
                'success': True
            })
        else:
            response.update({
                'success': False,
                'error_code': 1
            })
    except AuthSms.DoesNotExist:
        response.update({
            'success': False,
            'error_code': 2
        })

    return HttpResponse(json.dumps(response), return_type, return_status_code)
