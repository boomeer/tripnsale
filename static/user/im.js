function RefreshMsgs() {
    $.post("/user/im_msg_frame/", {
        peer: $("#peer").val(),
    }, function(res) {
        $(".msgs").html(res);
        $(".msgsWrapper").animate({ scrollTop: 2 * $(".msgsWrapper").height() }, "slow");
    });
}

$(function() {
    $(".sendBtn").on("click", function() {
        $.post("/user/im/", {
            act: "send",
            peer: $("#peer").val(),
            content: $("#msgContent").val(),
        }, function(res) {
            RefreshMsgs();
            $("#msgContent").val("");
        });
    });
    RefreshMsgs();
});
