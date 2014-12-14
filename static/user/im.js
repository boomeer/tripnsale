function ProcOpts(opts)
{
    if (opts.addGuarant != window.addGuarant) {
        window.addGuarant = opts.addGuarant;
        if (window.addGuarant) {
            $(".guarantBtn").show();
        }
        else {
            $(".guarantBtn").hide();
        }
    }
    SetUnread(opts.unreadCount);
}


function RefreshMsgs() {
    $.post("/user/im_msg_frame/", {
        conf: $("#conf").val(),
        read: window.isActive ? 1 : 0,
    }, function(res) {
        var oldMsgs = $(".msgs").html();
        var content = res.content;
        var opts = res.opts;
        if (content != oldMsgs) {
            $(".msgs").html(content);
            $("body").animate({ scrollTop: 2 * $("body").height() }, "fast");
        }
        ProcOpts(opts);
    });
}

function SendMsg()
{
    $("#msgContent").attr("disabled", "1");
    $.post("/user/im/", {
        act: "send",
        conf: $("#conf").val(),
        content: $("#msgContent").val(),
    }, function(res) {
        RefreshMsgs();
        $("#msgContent").val("").removeAttr("disabled").focus();
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

    window.addGuarant = false;
});
