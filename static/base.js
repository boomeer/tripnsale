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


$(function() {
    window.isActive = true;
    $(window).focus(function() { this.isActive = true; });
    $(window).blur(function() { this.isActive = false; });
});
