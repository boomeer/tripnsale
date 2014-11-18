function RefreshMsgs() {
    $.post("/user/im_msg_frame/", {
        peer: $("#peer").val(),
    }, function(res) {
        var oldMsgs = $(".msgs").html();
        if (res != oldMsgs) {
            $(".msgs").html(res);
            $("body").animate({ scrollTop: 2 * $("body").height() }, "slow");
        }
    });
}

function sendMsg()
{
    $.post("/user/im/", {
        act: "send",
        peer: $("#peer").val(),
        content: $("#msgContent").val(),
    }, function(res) {
        RefreshMsgs();
        $("#msgContent").val("");
    });
}

$(function() {
    $(".sendBtn").on("click", function() {
        sendMsg();
    });
    $("#msgContent").on("keydown", function(event) {
        if (event.which == 13) {
            sendMsg();
        }
    });
    RefreshMsgs();
    setInterval(function() {
        RefreshMsgs();
    }, 500);
});
