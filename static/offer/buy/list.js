function BuyChangeHref()
{
    var jthis = $(this);
    var chref = jthis.attr("href");
    var m = chref.match(/^\?page=(\d+)$/);
    if (!m || !m.length || m.length < 2) {
        return;
    }
    jthis.attr("href", "#buyspage" + m[1]);
    jthis.off("focus click mouseenter");
}

function BuyChangePage()
{
    if (window.location.hash.match(/^#buyspage\d+$/)) {
        BuyViewClose(true);
        if (BuyGetPage() != BuyGetRealPage()) {
            BuysRefresh();
        }
    } else if (window.location.hash.match(/^#buy\d+$/)) {
        BuyView(window.location.hash.slice(4), true);
    } else {
        BuyViewClose();
    }
}

$(function() {
    $(window).bind('hashchange', BuyChangePage);
    $("#buysFilterApply").on("click", BuysRefresh);
    $("#buysTitle").on("input", BuysRefresh);
    $("#buysFilterFrom").on("input", BuysRefresh);
    $("#buysFilterTo").on("input", BuysRefresh);

    if (BuyGetPage(null) != null && BuyGetPage() != BuyGetRealPage()) {
        BuysRefresh();
    } else {
        $(".pagination-link.pagination-static")
            .mouseenter(BuyChangeHref)
            .focus(BuyChangeHref)
            .click(function(e) {
                    BuyChangeHref.call(this);
                }
            );
    }

    $(".buy-item .full-info").hide();
    $(".owner.owner-right.buy-section").click(StopPropagationEvent);
    $(".profile-link").click(StopPropagationEvent);

    if (window.location.hash.match(/^#buy\d+$/)) {
        BuyView(window.location.hash.slice(4));
    }
});


