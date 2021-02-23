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
    if request.method == 'POST':
        business_number1 = request.POST.get('cn1')
        business_number2 = request.POST.get('cn2')
        business_number3 = request.POST.get('cn3')
        license_number = business_number1 + business_number2 + business_number3
        # todo : 사업자 번호 문자열 ㄴㄴ javascript 처리 하기
        try:
            ap = ApplicationForm.objects.filter(license_number=license_number)
            if ap:
                print('??')
            print(f'ap : {ap}')
            # todo: upload_to 부분 수정하기

        except Exception as e:
            pass

    context = {}
    return render(request, 'join/request.html', context)
