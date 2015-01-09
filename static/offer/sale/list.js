function TripChangePage()
{
    if (window.location.hash.match(/^#tripspage\d+$/)) {
        TripViewClose(true);
        if (TripsGetPage() != TripsGetRealPage()) {
            TripsRefresh();
        }
    } else if (window.location.hash.match(/^#trip\d+$/)) {
        TripView(window.location.hash.slice(5), true);
    } else {
        TripViewClose();
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
    $("#tripsFilterApply").on("click", TripsRefresh);
    $("#tripsFilterFrom").on("input", TripsRefresh);
    $("#tripsFilterTo").on("input", TripsRefresh);

    if (TripsGetPage(null) != null && TripsGetPage() != TripsGetRealPage()) {
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
    $(".tripOwner.tripOwner-right.tripSection").click(StopPropagationEvent);
    $(".profileLink").click(StopPropagationEvent);

    if (window.location.hash.match(/^#trip\d+$/)) {
        TripView(window.location.hash.slice(5));
    }
});
