$(document).ready(function() {
    $(document).on("keyup", "input:text[numberOnly]", function(){
        let replaceId = /[^0-9]/gi;
        let space: string = ""
        $(this).val($(this).val().toString().replace(replaceId, space));
    });

    $('button[name=check_duplicate_button]').click(function() {
        var company_number: string = $('input[name=cn1]').val() + '-' + $('input[name=cn2]').val() + '-' + $('input[name=cn3]').val();
        if (company_number.length == 0 || company_number == '') {
            $('[name=cn-message]').html('사업자번호를 입력해주세요.');
            $('[name=cn-message]').css('display', '');
            return;
        }

        var button = $(this);
        var input_company_number= $('input[name=company_number]');
        let message: string = '';

        $.ajax({
            url: '/ajax/join/license_number/validate/',
            type: 'POST',
            data: {'company_number': company_number},
            dataType: 'json',
            success: function(json) {
                if (json.success == false) {
                    button.attr('data-confirm', 0);

                    var error_code = json.error.code;

                    if (error_code == 'invalid_company_number') {
                        message = '사업자번호를 확인해주세요.';
                    } else if (error_code == 'is_duplicate') {
                        message = '이미 등록되어 있는 업체입니다.'
                    } else if (error_code == 'already_request') {
                        message = '이미 입점 신청되어 있는 업체입니다.'
                    }
                    $('[name=cn-message]').html(message);
                    $('[name=cn-message]').css('display', '');

                    input_company_number.val('');
                } else {
                    button.attr('data-confirm', 1);

                    $('[name=cn-message]').html('입점신청 가능합니다.');
                    $('[name=cn-message]').css('display', '');

                    input_company_number.val(company_number)
                }
            }
        });
    });

    var fileTarget = $('.upload-hidden');

    fileTarget.on('change', function(){
        if (window.FileReader){
            // 최신 브라우저
            var filename = (<HTMLInputElement>$(this)[0]).files[0].name;
        }
        else {
            // 예전 브라우저
            var filename = $(this).val().toString().split('/').pop().split('\\').pop();
        }

        $(this).siblings('.upload-name').val(filename);
    });

    $('.w-s').keyup(function(){
        var value = (<HTMLInputElement>$(this)[0]).value.length;
        var charLimit = $(this).attr('maxlength');
        if (value >= Number(charLimit)) {
            $(this).next().next('.w-s').focus();
            return false;
        }
    });
});