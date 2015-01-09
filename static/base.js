var prevOverflow = null;
var scrollPosition = null;

function PreventDefaultEvent(e) { e.preventDefault(); }
function StopPropagationEvent(e) { e.stopPropagation(); }
function LockScroll(){
    $html = $('html');
    $body = $('body');
    var initWidth = $body.outerWidth();
    var initHeight = $body.outerHeight();

    scrollPosition = [
        self.pageXOffset || document.documentElement.scrollLeft || document.body.scrollLeft,
        self.pageYOffset || document.documentElement.scrollTop  || document.body.scrollTop
    ];
    prevOverflow = $html.css('overflow');
    $html.css('overflow', 'hidden');
    window.scrollTo(scrollPosition[0], scrollPosition[1]);

    var marginR = $body.outerWidth()-initWidth;
    var marginB = $body.outerHeight()-initHeight;
    $body.css({'margin-right': marginR,'margin-bottom': marginB});
}

function UnlockScroll(){
    if (prevOverflow === null || scrollPosition === null) {
        console.log("dfgdfsg");
        return;
    }
    $html = $('html');
    $body = $('body');
    $html.css('overflow', "");
    window.scrollTo(scrollPosition[0], scrollPosition[1]);

    $body.css({'margin-right': 0, 'margin-bottom': 0});
}

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
