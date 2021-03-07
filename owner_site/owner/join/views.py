import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from app.models import ApplicationForm


def process(request) -> HttpResponse:
    context = {}
    return render(request, 'join/process.html', context)


@csrf_exempt
def online_entry(request) -> HttpResponse:
    context = {}
    phone_first_numbers = ['010', '011', '016', '017', '018', '019', '0130']

    context.update({
        'phone_first_numbers': phone_first_numbers
    })

    return render(request, 'join/request.html', context)


@csrf_exempt
def ajax_license_validate(request) -> HttpResponse:
    license_number = request.POST.get('company_number')
    return_type = 'application/json'
    return_status_code = 200
    response = {}

    license_number_len = len(license_number.replace("-", ""))
    if license_number_len != 10:
        response.update({
            'success': False,
            'error': {
                'code': 'invalid_company_number'
            }
        })
    else:
        af = ApplicationForm.objects.filter(license_number=license_number)
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
    return_type = 'application/json'
    return_status_code = 200
    response = {}
    phone_number = request.POST.get('mobile_phone_number')

    return HttpResponse(json.dumps(response), return_type, return_status_code)
