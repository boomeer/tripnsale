function BuysRefresh(user, profile)
{        
    $(".buysList").html("Загрузка...");
    $.post("/offer/buy/filter/", {
        "title": $("#buysTitle").val(),
        "owner": user ? user : 0,
        "profile": profile,
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

function BuyViewClose()
{
    window.location.hash = "";
    $(".buyViewWrapper").html("");
}


$(function() {
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

    if (window.location.hash) {
        BuyView(window.location.hash.slice(1));
    }
});


