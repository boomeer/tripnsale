function TripsRefresh()
{        
    $(".tripsList").html("Загрузка...");
    $.post("/sale/filter/", {
        "from": $("#tripsFilterFrom").val(),
        "to": $("#tripsFilterTo").val(),
    }, function(res) {
        $(".tripsList").html(res);
    });
}


$(document).ready(function() {
    $("#tripsFilterApply").on("click", function() {
        TripsRefresh();
    });
    $("#tripsFilterFrom").on("input", function() {
        TripsRefresh();
    });

    $("#allPagesWrapper").fullpage();
});
