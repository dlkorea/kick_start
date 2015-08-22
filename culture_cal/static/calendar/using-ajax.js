var write_reply = function() {
    $('#write_reply_form').submit(function( event ){
        event.preventDefault();

        var self = $(this),
            url = self.data('url_address'),
            //author = self.find('#id_author').val(),
            content = self.find('#id_content').val();

        var processServerResponse = function(serverResponseData) {
            $('.reply_area').html(serverResponseData);
            replyCount = $('#comment_count').html().replace(/[^0-9]/g, '');
            $('#reply_count_in_header').find('b').html(replyCount);
            startupFunction();
        };

        var config = {
                url : url,
                type : "POST",
                data : {
                    content : content,
                },
                datatype : 'html',
                success : processServerResponse,
        };
        if (content != '') {
            $.ajax(url, config);
        } else {
            $('#id_content').focus();
            alert('댓글을 입력하세요.');
        };
    });
};

var article_like = function() {
    $('.article_like_buttons').children().click( function () {
            var id = $(this).attr('id').replace(/[^0-9]/g, '');
            var action = $(this).attr('class');
            var url = $(this).parent().data('url_address');

        if (action == 'like') {
            var ment = '추천 하시겠습니까?';
        } else if (action == 'dislike') {
            var ment = '비추천 하시겠습니까?';
        }
        if (confirm(ment)) {
            var processServerResponse = function(serverResponseData) {
            if (serverResponseData.status == 'done') {
                // 버튼 바꾸고
                $('#article-like-'+id).html('추천 '+serverResponseData.like);
                $('#article-dislike-'+id).html('비추천 '+serverResponseData.dislike);
                // article_header에 숫자들 바꾸고
                $('#like_count_in_header').find('b').html(serverResponseData.like);
                $('#dislike_count_in_header').find('b').html(serverResponseData.dislike);
            } else if (serverResponseData.status == 'done_before') {
                alert('이미 투표하셨습니다.');
            }};
            var config = {
                        url : url,
                        type : "POST",
                        data : {
                            target : 'article',
                            id : id,
                            action : action,
                        },
                        datatype : 'json',
                        success : processServerResponse,
            };
            $.ajax(url, config);
        };
    })
}
var reply_like = function() {
    $('.reply_like_buttons').children().click( function () {
        var id = $(this).attr('id').replace(/[^0-9]/g, '');
        var action = $(this).attr('class');
        var url = $(this).parent().data('url_address');

        if (action == 'like') {
            var ment = '추천 하시겠습니까?';
        } else if (action == 'dislike') {
            var ment = '비추천 하시겠습니까?';
        }
        if (confirm(ment)) {
            var processServerResponse = function(serverResponseData) {
            if (serverResponseData.status == 'done') {
                // 버튼 바꾸고
                $('#reply-like-'+id).html('추천 '+serverResponseData.like);
                $('#reply-dislike-'+id).html('비추천 '+serverResponseData.dislike);
            } else if (serverResponseData.status == 'done_before') {
                alert('이미 투표하셨습니다.');
            }};

            var config = {
                        url : url,
                        type : "POST",
                        data : {
                            target : 'reply',
                            id : id,
                            action : action,
                        },
                        datatype : 'json',
                        success : processServerResponse,
            };
            $.ajax(url, config);
        }
    })
}

var deleteReply = function (url) {
    var processServerResponse = function(serverResponseData) {
        $('.reply_area').html(serverResponseData);
        startupFunction();
    }
    var config = {
                url : url,
                type : "GET",
                datatype : 'html',
                success : processServerResponse,
    };
    $.ajax(url, config);
}

var startupFunction = function() {
    write_reply();
    article_like();
    reply_like();
    $('.write_reply').find('#id_content').attr('onkeydown','resize(this)');
    $('.edit_reply').find('#id_content').attr('onkeydown','resize(this)');
};


$(document).ready(function() {
    startupFunction();
});
