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
        $(".tripsList").html(res);
    });
}

function TripView(id)
{
    window.location.hash = "#trip" + id;
    $.post("/offer/sale/view/" + id, {}, function(res) {
        LockScroll();
        $(".tripViewWrapper").html(res);
    });
}

function TripViewClose(changehash)
{
    window.location.hash = "";
    $(".tripViewWrapper").html("");
    UnlockScroll();
}

function TripRemove(id)
{
    if (confirm("Вы действительно хотите удалить поездку?")) {
        window.location.href = "/offer/sale/remove/?id=" + id + "&backref=/offer/sale/list/";
    }
}


function TripChangePage()
{
    if (window.location.hash.match(/^#tripspage\d+$/)) {
        TripsRefresh();
        UnlockScroll();
    } else if (window.location.hash.match(/^#trip\d+$/)) {
        TripView(window.location.hash.slice(5));
    } else {
        $(".tripViewWrapper").html("");
        UnlockScroll();
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

    if (TripsGetPage(null) != null && TripsGetPage() != $("#tripsPage").val()) {
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
