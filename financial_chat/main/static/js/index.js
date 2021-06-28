var messages = [];

$(document).ready(function() {
    setInterval (refreshChat, 2500);

    $('#messageform').submit(function(event){
        event.preventDefault();
        var formData = new FormData($(this)[0]);
        $.ajax({
            type: 'POST',
            url: 'messages/create/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data){
                if (data['error']==0){
                    //message('success', data['detail']);
                    refreshChat(formData)
                } else{
                    //message('danger', data['detail']);
                }
            }
        }).fail(function(e){
            //message('danger',e.statusText);
        });
        $('#usermsg').val('');

        return false;
    });
});

function refreshChat(form){
    $.ajax({
        url: 'messages/list/',
        type: 'GET',
        data: {'chat': 1},
        success: function(data){
            console.table(data);
            messages = data;
            drawChat();
        }
    });
}

function drawChat(){
    let html = '';
    for (var i = messages.length - 1; i >= 0; i--) {
        let time = messages[i].registration_date;
        let user = messages[i].user.username;
        let content = messages[i].content;

        html += ''
        +'<div class="chatmessage"><span class="chattime">' + time
        +'</span><b class="chatusername">' + user
        +'</b><span class="chatcontent">' + content
        +'</span><br></div>'
    }
    $("#chatbox").html(html)
}



