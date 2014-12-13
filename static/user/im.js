function RefreshMsgs() {
    $.post("/user/im_msg_frame/", {
        conf: $("#conf").val(),
    }, function(res) {
        var oldMsgs = $(".msgs").html();
        if (res != oldMsgs) {
            $(".msgs").html(res);
            $("body").animate({ scrollTop: 2 * $("body").height() }, "slow");
        }
    });
}

function SendMsg()
{
    $.post("/user/im/", {
        act: "send",
        conf: $("#conf").val(),
        content: $("#msgContent").val(),
    }, function(res) {
        RefreshMsgs();
        $("#msgContent").val("");
    });
}

function AskGuarant()
{
    $.post("/user/im/", {
        act: "askGuarant",
        conf: $("#conf").val(),
    }, function(res) {
        RefreshMsgs();
    });
}

$(function() {
    $(".sendBtn").on("click", function() {
        SendMsg();
    });
    $(".guarantBtn").on("click", function() {
        AskGuarant();
    });
    $("#msgContent").on("keydown", function(event) {
        if (event.which == 13) {
            SendMsg();
        }
    });
        RefreshMsgs();
    setInterval(function() {
        RefreshMsgs();
    }, 500);
});
