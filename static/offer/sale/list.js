function TripsRefresh()
{        
    $(".tripsList").html("Загрузка...");
    $.post("/offer/sale/filter/", {
        "from": $("#tripsFilterFrom").val(),
        "to": $("#tripsFilterTo").val(),
    }, function(res) {
        $(".tripsList").html(res);
    });
}

function TripView(id)
{
    $.post("/offer/sale/view/" + id, {}, function(res) {
        $(".tripViewWrapper").html(res);
    });
}

function TripViewClose()
{
    $(".tripViewWrapper").html("");
}


$(function() {
    $("#tripsFilterApply").on("click", function() {
        TripsRefresh();
    });
    $("#tripsFilterFrom").on("input", function() {
        TripsRefresh();
    });

    TripsRefresh();
});
