function BuyGetPage(defultPage)
{
    if (typeof defaultPage == "undefined") {
        defaultPage = 1;
    }
    var found = window.location.hash.match(/^#buyspage(\d+)$/);
    return (!found ? defaultPage : found[1]*1);
}

function BuyGetRealPage()
{
    return $("#buysPage").val();
}

function BuysRefresh()
{
    var bp = $("#buysProfile");
    var bo = $("#buysOwner");
    var fr = $("#buysFilterFrom");
    var to = $("#buysFilterTo");
    $(".buysList").html("Загрузка...");
    $(".buyViewWrapper").html("");
    $.post("/offer/buy/filter/", {
        "title": $("#buysTitle").val(),
        "fr": fr ? fr.val() : "",
        "to": to ? to.val() : "",
        "profile": bp ? bp.val() : "",
        "page": BuyGetPage(),
        "owner": bo ? bo.val() : 0
    }, function(res) {
        $(".buysList").html(res);
    });
}

function BuyView(id, notChangeHash)
{
    if (!notChangeHash) {
        window.location.hash = "#buy" + id;
    }
    $.post("/offer/buy/view/" + id, {}, function(res) {
        $(".buyViewWrapper").html(res);
        LockScroll();
    });
}

function BuyRemove(id)
{
    if (confirm("Вы действительно хотите удалить заказ?")) {
        window.location.href = "/offer/buy/remove/?id=" + id + "&backref=/offer/buy/list/";
    }
}

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

function BuyViewClose(notChangeHash)
{
    if (!notChangeHash) {
        window.location.hash = "#buyspage" + BuyGetRealPage();
    }
    $(".buyViewWrapper").html("");
    UnlockScroll();
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


