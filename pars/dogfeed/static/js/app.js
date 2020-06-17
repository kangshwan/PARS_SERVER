$(document).ready(function(){
    $.ajax({
        type: "GET",
        timeout: 100000
    });
    $("#changepet").click(function(){
        $("#mydog").html("dog");
    });
});
