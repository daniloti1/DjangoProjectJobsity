$(document).ready(function(){
    $("#ver-pass").click(function(){
        var password = $("#password-lg");
        if(password.attr("type") == "password"){
        password.attr("type","text");
        $("#eye").removeClass("fa-eye");
        $("#eye").addClass("fa-eye-slash");
        } else{
        password.attr("type","password");
        $("#eye").removeClass("fa-eye-slash");
        $("#eye").addClass("fa-eye");
        }
    });
});