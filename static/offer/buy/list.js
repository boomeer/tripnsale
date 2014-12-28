function GetPage()
{
    var found = window.location.hash.match(/^#page(\d+)$/);
    return (!found ? 1 : found[1]*1);
}

function BuysRefresh()
{
    var bo = $("#buysOwner");
    var bp = $("#buysProfile");
    $(".buysList").html("Загрузка...");
    $.post("/offer/buy/filter/", {
        "title": $("#buysTitle").val(),
        "owner": bo ? bo.val() : "",
        "profile": bo ? bo.val() : "",
        "page": GetPage() - 1
    }, function(res) {
        $(".buysList").html(res);
    });
}

function BuyView(id)
{
    window.location.hash = "#" + id;
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

function ChangePage()
{
    if (window.location.hash.match(/^#page\d+$/)) {
        BuysRefresh();
    }
}

$(function() {
    $(window).bind('hashchange', ChangePage);
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

    if (window.location.hash.match(/^#\d+&/)) {
        BuyView(window.location.hash.slice(1));
    }
});


