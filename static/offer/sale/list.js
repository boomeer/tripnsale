function TripsGetPage()
{
    var found = window.location.hash.match(/^#tripspage(\d+)$/);
    return (!found ? 1 : found[1]*1);
}

function TripsRefresh()
{
    var sp = $("#tripsProfile");
    var so = $("#tripsOwner");
    var fr = $("#tripsFilterFrom");
    var to = $("#tripsFilterTo");
    $(".tripsList").html("Загрузка...");
    $(".tripViewWrapper").html("");
    $.post("/offer/sale/filter/", {
        "from": fr ? fr.val() : "",
        "to": to ? to.val() : "",
        "profile": sp ? sp.val() : 0,
        "page": TripsGetPage() - 1,
        "owner": so ? so.val() : 0
    }, function(res) {
        $(".tripsList").html(res);
    });
}

function TripView(id)
{
    window.location.hash = "#trip" + id;
    $.post("/offer/sale/view/" + id, {}, function(res) {
        $(".tripViewWrapper").html(res);
    });
}

function TripViewClose(changehash)
{
    window.location.hash = "";
    $(".tripViewWrapper").html("");
}


function TripChangePage()
{
    if (window.location.hash.match(/^#tripspage\d+$/)) {
        TripsRefresh();
    } else if (window.location.hash.match(/^#trip\d+$/)) {
        TripView(window.location.hash.slice(5));
    } else {
        $(".tripViewWrapper").html("");
    }
}

$(function() {
    $(window).bind('hashchange', TripChangePage);
    $("#tripsFilterApply").on("click", function() {
        TripsRefresh();
    });
    $("#tripsFilterFrom").on("input", function() {
        TripsRefresh();
    });
    $("#tripsFilterTo").on("input", function() {
        TripsRefresh();
    });

    var block = $("#blockStartupList");
    if (!(block && block.val() == 1)) {
        TripsRefresh();
    }

    if (window.location.hash.match(/^#trip\d+$/)) {
        TripView(window.location.hash.slice(5));
    }
});
