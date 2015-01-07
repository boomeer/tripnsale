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
    if (opts.toWithGuarant != window.toWithGuarant) {
        window.toWithGuarant = opts.toWithGuarant;
        if (window.toWithGuarant) {
            $(".toWithGuarantBtn").on("click", function() {
                window.location.href = window.toWithGuarant;
            });
            $(".toWithGuarantBtn").show();
        }
        else {
            $(".toWithGuarantBtn").hide();
        }
    }
    if (opts.toWithoutGuarant != window.toWithoutGuarant) {
        window.toWithoutGuarant = opts.toWithoutGuarant;
        if (window.toWithoutGuarant) {
            $(".toWithoutGuarantBtn").on("click", function() {
                window.location.href = window.toWithoutGuarant;
            });
            $(".toWithoutGuarantBtn").show();
        }
        else {
            $(".toWithoutGuarantBtn").hide();
        }
    }
    SetUnread(opts.unreadCount);
}

function ScrollToBottom()
{
    $("html,body").animate({ scrollTop: $(".msgsWrapper").height() + $("body").height() }, "fast");
}

function RefreshMsgs(scroll) {
    $.post("/user/im_msg_frame/", {
        conf: $("#conf").val(),
        read: window.isActive ? 1 : 0,
    }, function(res) {
        var oldMsgs = $(".msgs").html();
        var content = res.content;
        var opts = res.opts;
        if (content != oldMsgs) {
            $(".msgs").html(content);
            if (scroll) {
                ScrollToBottom();
            }
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
        RefreshMsgs(true);
        $("#msgContent").val("").removeAttr("disabled").focus();
    });
}

function AskGuarant()
{
    $.post("/user/im/", {
        act: "askGuarant",
        conf: $("#conf").val(),
    }, function(res) {
        RefreshMsgs(true);
    });
}

$(function() {
    $(".msgsWrapper").css("margin-bottom", $(".imfooter-wrap").height() + "px");
    $(".sendBtn").on("click", SendMsg);
    $(".guarantBtn").on("click", AskGuarant);
    $("#msgContent").on("keydown", function(event) {
        if (event.which == 13) {
            SendMsg();
        }
    });

    RefreshMsgs(true);
    setInterval(function() {
        RefreshMsgs(false);
    }, 500);

    window.addGuarant = false;

    $("#msgContent").focus();
});
