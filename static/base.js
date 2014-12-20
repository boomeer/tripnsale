function RefrUnread()
{
    if (window.unread) {
        $(".unread-count").html("+" + window.unread);
        $(".unread-count-wrapper").show();
    }
    else {
        $(".unread-count-wrapper").hide();
    }
}

function SetUnread(unread)
{
    if (window.unread != unread) {
        window.unread = unread;
        RefrUnread();
    }
}

function CheckFooter() {
    var h = $("body").height() - $(".footer").outerHeight(true);
    $(".main-wrap").css("min-height", h);
}

function CheckHeader() {
    $(".main").css("margin-top", $("header").outerHeight());
    $(".page-wrap2").css("margin-top", -$("header").outerHeight());
}

$(function() {
    window.isActive = true;
    $(window).focus(function() { this.isActive = true; });
    $(window).blur(function() { this.isActive = false; });
    $(window).resize(CheckFooter);
    $(window).resize(CheckHeader);

    // oh my god
    setTimeout (CheckFooter, 100);
    setTimeout (CheckHeader, 100);
});
