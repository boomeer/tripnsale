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
        $(".owner.owner-right.buy-section").click(StopPropagationEvent);
        $(".profile-link").click(StopPropagationEvent);
        $(".fast-profile-btn").click(StopPropagationEvent);
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

function BuyViewClose(notChangeHash)
{
    if (!notChangeHash) {
        window.location.hash = "#buyspage" + BuyGetRealPage();
    }
    $(".buyViewWrapper").html("");
    UnlockScroll();
}
