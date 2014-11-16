function BuysRefresh()
{        
    $(".buysList table tbody").html("Загрузка...");
    $.post("/offer/buy/filter/", {
        "title": $("#buysTitle").val(),
    }, function(res) {
        $(".buysList table tbody").html(res);
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

    BuysRefresh();
});
