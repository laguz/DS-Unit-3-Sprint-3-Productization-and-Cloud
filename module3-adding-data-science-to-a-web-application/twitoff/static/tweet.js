$('#author_text_input').value="Please enter a twitter user's handle";
$('#author_submit').click(function(){
    $.ajax({
      url:'/add_user?twitter_handle=' + $('#author_text_input').val(),
      type: 'GET',
    });
});
$('#tweet_text_input').value="Please enter a twitter to classify";
$('#tweet_submit').click(function(){
    $.ajax({
      url:'/predict_author?tweet_to_classify=' + $('#tweet_text_input').val(),
      type: 'GET',
      success: function(){
        $('tweet_text_input').innerText = <response.text>
      }
    });
});
