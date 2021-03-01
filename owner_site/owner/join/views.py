import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from app.models import ApplicationForm


def process(request) -> dict:
    context = {}
    return render(request, 'join/process.html', context)


@csrf_exempt
def online_entry(request):
    """
    - 사업자 정보
        - 사업자 번호
        - 사업자등록증 사본등록
        - 영업신고증 사본등록
        - 사업주 명
        - 사업자 휴대폰 번호
        - 인증번호 입력
    - 음식점 정보
        - 음식점 이름
        - 음식점 전화번호
        - 음식점 주소
        - 업종 카테고리
        - 배달 가능 여부
        - 전단지 등록

    """
    context = {}

    return render(request, 'join/request.html', context)


@csrf_exempt
def ajax_license_validate(request):
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
