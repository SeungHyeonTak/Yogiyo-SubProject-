$(document).ready(function () {
    $(document).on("keyup", "input:text[numberOnly]", function () {
        var replaceId = /[^0-9]/gi;
        var space = "";
        $(this).val($(this).val().toString().replace(replaceId, space));
    });
    $('button[name=check_duplicate_button]').click(function () {
        var company_number = $('input[name=cn1]').val() + '-' + $('input[name=cn2]').val() + '-' + $('input[name=cn3]').val();
        if (company_number.length == 0 || company_number == '') {
            $('[name=cn-message]').html('사업자번호를 입력해주세요.');
            $('[name=cn-message]').css('display', '');
            return;
        }
        var button = $(this);
        var input_company_number = $('input[name=company_number]');
        var message = '';
        $.ajax({
            url: '/ajax/join/license_number/validate/',
            type: 'POST',
            data: { 'company_number': company_number },
            dataType: 'json',
            success: function (json) {
                if (json.success == false) {
                    button.attr('data-confirm', 0);
                    var error_code = json.error.code;
                    if (error_code == 'invalid_company_number') {
                        message = '사업자번호를 확인해주세요.';
                    }
                    else if (error_code == 'is_duplicate') {
                        message = '이미 등록되어 있는 업체입니다.';
                    }
                    else if (error_code == 'already_request') {
                        message = '이미 입점 신청되어 있는 업체입니다.';
                    }
                    $('[name=cn-message]').html(message);
                    $('[name=cn-message]').css('display', '');
                    input_company_number.val('');
                }
                else {
                    button.attr('data-confirm', 1);
                    $('[name=cn-message]').html('입점신청 가능합니다.');
                    $('[name=cn-message]').css('display', '');
                    input_company_number.val(company_number);
                }
            }
        });
    });
    var fileTarget = $('.upload-hidden');
    fileTarget.on('change', function () {
        if (window.FileReader) {
            // 최신 브라우저
            var filename = $(this)[0].files[0].name;
        }
        else {
            // 예전 브라우저
            var filename = $(this).val().toString().split('/').pop().split('\\').pop();
        }
        $(this).siblings('.upload-name').val(filename);
    });
    $('.w-s').keyup(function () {
        var value = $(this)[0].value.length;
        var charLimit = $(this).attr('maxlength');
        if (value >= Number(charLimit)) {
            $(this).next().next('.w-s').focus();
            return false;
        }
    });
    $('button[name=send_veri_code_button]').click(function () {
        var mobile_phone_number = $('input[name=mobile_phone_number]').toString();
        var phone_number = $('select[name=mtel1]').val().toString() + $('input[name=mtel2]').val().toString() + $('input[name=mtel3]').val();
        mobile_phone_number = phone_number;
        $.ajax({
            url: '/ajax/join/phone_number_sms/authentication/',
            type: 'POST',
            dataType: 'json',
            data: { 'mobile_phone_number': mobile_phone_number },
            success: function (json) {
                if (json.success == false) {
                    console.log('False');
                }
                else {
                    console.log('True');
                }
            }
        });
    });
    $('button[name=comfirm_veri_code_button]').click(function () {
        var confirm_button = $(this);
        var confirm_veri_code_message = $('[name=confirm_veri_code_message]');
        var phone_number = $('select[name=mtel1]').val().toString() + $('input[name=mtel2]').val().toString() + $('input[name=mtel3]').val();
        var code = $('input[name=veri_code]').val();
        var message = '';
        $.ajax({
            url: '/ajax/join/sms_code_validate/',
            type: 'POST',
            dataType: 'json',
            data: { 'code': code, 'phone_number': phone_number },
            success: function (json) {
                if (json.success == true) {
                    confirm_button.attr('data-confirm', 1);
                    confirm_veri_code_message.html('인증이 확인되었습니다.');
                    confirm_veri_code_message.css('display', '');
                }
                else {
                    console.log(confirm_button.attr('data-confirm', 0));
                    confirm_button.attr('data-confirm', 0);
                    if (json.error_code == 1) {
                        console.log('check');
                        message = '인증번호 입력 시간이 초과되었습니다. 인증번호 받기 버튼을 눌러주세요.';
                    }
                    else {
                        message = '인증번호가 일치하지 않습니다. 다시 시도해 주세요.';
                    }
                    confirm_veri_code_message.html(message);
                    confirm_veri_code_message.css('display', '');
                }
                console.log('end');
            }
        });
    });
});
