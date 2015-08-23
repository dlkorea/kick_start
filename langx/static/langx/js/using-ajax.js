$.fn.exists = function () {
    return this.length !== 0;
};

var write_question = function() {
    $('#write_form').on('submit', function(event){
        event.preventDefault();
        var self = $(this),
            url = self.attr('action'),
            content = self.find("textarea").val();

        if ( ! $('#header').find('#logout').exists() ) {
            $('#myModal').modal('show');
        } else if(content) {
            $.ajax({
                url: url,
                method: "POST",
                data: {
                    content: content,
                },
            }).done(function(html) {
                self.find('textarea').val('');
                $('.question_area').prepend(html);
            }).fail(function(){
                alert('fail!!');
            });
        };
        return false;
    });
}

var write_answer = function() {
    $('.write_answer').on('submit', function(event){
      event.preventDefault();
      var self = $(this);
      var question_pk = self.data('pk');
      //alert(question_pk);
      //alert(self.attr('action'));
      if ( ! $('#header').find('#logout').exists() ) {
        $('#myModal').modal('show');
      } else if(self.find('#id_content').val()) {
        var url = self.attr('action'),
            content = self.find('#id_content').val();

        $.ajax({
            url: url,
            method: "POST",
            data: {
                content: content,
            },
        }).done(function(html) {
            $('#answer_area_'+question_pk).append(html);
            self.find('#id_content').val('');
        }).fail(function() {
            alert('fail');
        }
        );

        return false;
      }
    })
}
var answer_like = function() {
    $('.like_answer').on('click', function(event) {
        event.preventDefault();
        var url = $(this).attr('href');
        var answer_pk = $(this).data('answer_pk');
        var like_answer_self = $(this);

        if ( ! $('#header').find('#logout').exists() ) {
            $('#myModal').modal('show');
        } else {
            $.ajax({
                url: url,
                method:"POST",
                pk: answer_pk,
            }).done(function(data) {
                var dataStr = '<i class="fa fa-thumbs-o-up"></i> '+data.liked_user_number;
                like_answer_self.html(dataStr);
            }).fail(function(err) {
                alert(err);
            });
        }
        return false;
    })
}


