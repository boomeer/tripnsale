function BuyGetPage()
{
    var found = window.location.hash.match(/^#buyspage(\d+)$/);
    return (!found ? 1 : found[1]*1);
}

function BuysRefresh()
{
    var bp = $("#buysProfile");
    var bo = $("#buysOwner");
    $(".buysList").html("Загрузка...");
    $(".buyViewWrapper").html("");
    $.post("/offer/buy/filter/", {
        "title": $("#buysTitle").val(),
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

function BuyViewClose()
{
    window.location.hash = "";
    $(".buyViewWrapper").html("");
}

function BuyChangePage()
{
    alert(window.location.hash);
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

    var block = $("#blockStartupList");
    if (!(block && block.val() == 1)) {
        BuysRefresh();
    }

    if (window.location.hash.match(/^#buy\d+$/)) {
        BuyView(window.location.hash.slice(4));
    }
});


