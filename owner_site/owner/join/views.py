from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.models import ApplicationForm


def process(request):
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
    # todo : 사업자 번호 문자열 ㄴㄴ javascript 처리 하기
    context = {}

    if request.method == 'POST':
        license_number = f'{request.POST.get("cn1")}-{request.POST.get("cn2")}-{request.POST.get("cn3")}'
        print(f'license_number : {license_number}')
        try:
            af_check = ApplicationForm.objects.filter(license_number=license_number)
            if af_check:
                context.update({
                    'error': '이미 등록되어 있는 업체입니다.',
                    'license_number': license_number
                })
            elif not af_check:
                context.update({
                    'success': '입점신청 가능합니다.',
                    'license_number': license_number
                })
            else:
                context.update({'none': '사업자번호를 확인해주세요.'})

        except Exception as e:
            pass
        print(f'context : {context}')

    return render(request, 'join/request.html', context)
