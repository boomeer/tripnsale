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
    var h = $("html").height() - $(".header").height() - $(".footer").height() - 80 + 34;
    // if (h > $(".main").height())
        $(".main-wrap").height(Math.max(h, $(".main").height()));
}

$(function() {
    window.isActive = true;
    $(window).focus(function() { this.isActive = true; });
    $(window).blur(function() { this.isActive = false; });
    // $(".main").resize(CheckFooter);
    // $(window).resize(CheckFooter);
    // CheckFooter();
    var h = $("html").height() - $(".header").height() - $(".footer").height() + 25;
    $(".main-wrap").css("min-height", h);
});
