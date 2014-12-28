function BuyGetPage()
{
    var found = window.location.hash.match(/^#buyspage(\d+)$/);
    return (!found ? 1 : found[1]*1);
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
        "from": fr ? fr.val() : "",
        "to": to ? to.val() : "",
        "profile": bp ? bp.val() : "",
        "page": BuyGetPage() - 1,
        "owner": bo ? bo.val() : 0
    }, function(res) {
        $(".buysList").html(res);
    });
}

function BuyView(id)
{
    window.location.hash = "#buy" + id;
    $.post("/offer/buy/view/" + id, {}, function(res) {
        $(".buyViewWrapper").html(res);
    });
}

function BuyRemove(id)
{
    if (confirm("Вы действительно хотите удалить заказ?")) {
        window.location.href = "/offer/buy/remove/?id=" + id + "&backref=/offer/buy/list/";
    }
}


function BuyViewClose()
{
    window.location.hash = "";
    $(".buyViewWrapper").html("");
}

function BuyChangePage()
{
    if (window.location.hash.match(/^#buyspage\d+$/)) {
        BuysRefresh();
    } else if (window.location.hash.match(/^#buy\d+$/)) {
        BuyView(window.location.hash.slice(4));
    } else {
        $(".buyViewWrapper").html("");
    }
}

$(function() {
    $(window).bind('hashchange', BuyChangePage);
    $("#buysFilterApply").on("click", function() {
        BuysRefresh();
    });
    $("#buysTitle").on("input", function() {
        BuysRefresh();
    });
    $("#buysFilterFrom").on("input", function() {
        BuysRefresh();
    });
    $("#buysFilterTo").on("input", function() {
        BuysRefresh();
    });

    var block = $("#blockStartupList");
    if (!(block && block.val() == 1)) {
        BuysRefresh();
    }

    if (window.location.hash.match(/^#buy\d+$/)) {
        BuyView(window.location.hash.slice(4));
    }
});


