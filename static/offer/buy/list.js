function BuysRefresh(user)
{        
    $(".buysList").html("Загрузка...");
    $.post("/offer/buy/filter/", {
        "title": $("#buysTitle").val(),
        "owner": user ? user : 0,
    }, function(res) {
        $(".buysList").html(res);
    });
}

function BuyView(id)
{
    $.post("/offer/buy/view/" + id, {}, function(res) {
        $(".buyViewWrapper").html(res);
    });
}

function BuyViewClose()
{
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
});
