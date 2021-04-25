$('#author_submit').click(function () {
    $.ajax({
        url: '/add_user?twitter_handle=' + $('#author_name_input').val(),
        type: 'GET',
    });
});
$('#tweet_submit').click(function () {
    $.ajax({
        url: '/predict_author?tweet_to_classify=' + $('#tweet_text_input').val(),
        type: 'GET',
        success: function (response){
            $('#classify_response').html(response)
        }
    });
});
