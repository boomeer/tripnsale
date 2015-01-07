function TripsGetPage(defaultPage)
{
    if (typeof defaultPage == "undefined") {
        defaultPage = 1;
    }
    var found = window.location.hash.match(/^#tripspage(\d+)$/);
    return (!found ? defaultPage : found[1]*1);
}

function TripsRefresh()
{
    console.log("TripsRefresh::begin!");
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
        "page": TripsGetPage(),
        "owner": so ? so.val() : 0
    }, function(res) {
        console.log("TripsRefresh::gotha!");

        $(".tripsList").html(res);
    });
}

function TripView(id)
{
    console.log("TripsView!");
    window.location.hash = "#trip" + id;
    $.post("/offer/sale/view/" + id, {}, function(res) {
        $(".tripViewWrapper").html(res);
    });
    lockScroll();
}

function TripViewClose(changehash)
{
    console.log("TripsViewClose!");
    window.location.hash = "";
    $(".tripViewWrapper").html("");
    unlockScroll();
}

function TripRemove(id)
{
    if (confirm("Вы действительно хотите удалить поездку?")) {
        window.location.href = "/offer/sale/remove/?id=" + id + "&backref=/offer/sale/list/";
    }
}


function TripChangePage()
{
    console.log("TripsChangePage!");
    if (window.location.hash.match(/^#tripspage\d+$/)) {
        TripsRefresh();
        unlockScroll();
    } else if (window.location.hash.match(/^#trip\d+$/)) {
        TripView(window.location.hash.slice(5));
    } else {
        $(".tripViewWrapper").html("");
        unlockScroll();
    }
}

function TripChangeHref()
{
    var jthis = $(this);
    var chref = jthis.attr("href");
    var m = chref.match(/^\?page=(\d+)$/);
    if (!m || !m.length || m.length < 2) {
        return;
    }
    jthis.attr("href", "#tripspage" + m[1]);
    jthis.off("focus click mouseenter");
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

    if (TripsGetPage(null) != null) {
        TripsRefresh();
    } else {
        $(".pagination-link.pagination-static")
            .mouseenter(TripChangeHref)
            .focus(TripChangeHref)
            .click(function(e) {
                    TripChangeHref.call(this);
                }
            );
    }

    $(".tripItem .fullInfo").hide();
    $(".tripOwner.tripOwner-right.tripSection").click(function(e) {
        e.stopPropagation();
    });

    if (window.location.hash.match(/^#trip\d+$/)) {
        TripView(window.location.hash.slice(5));
    }
});
