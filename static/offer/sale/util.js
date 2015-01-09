function TripsGetPage(defaultPage)
{
    if (typeof defaultPage == "undefined") {
        defaultPage = 1;
    }
    var found = window.location.hash.match(/^#tripspage(\d+)$/);
    return (!found ? defaultPage : found[1]*1);
}

function TripsGetRealPage()
{
    return $("#tripsPage").val();
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
        $(".fast-profile-btn").click(StopPropagationEvent);
        $(".tripOwner.tripOwner-right.tripSection").click(StopPropagationEvent);
        $(".profileLink").click(StopPropagationEvent);
    });
}

function TripView(id, notChangeHash)
{
    if (!notChangeHash) {
        window.location.hash = "#trip" + id;
    }
    $.post("/offer/sale/view/" + id, {}, function(res) {
        LockScroll();
        $(".tripViewWrapper").html(res);
    });
}

function TripViewClose(notChangeHash)
{
    if (!notChangeHash) {
        window.location.hash = "#tripspage" + TripsGetRealPage();
    }
    $(".tripViewWrapper").html("");
    UnlockScroll();
}

function TripRemove(id)
{
    if (confirm("Вы действительно хотите удалить поездку?")) {
        window.location.href = "/offer/sale/remove/?id=" + id + "&backref=/offer/sale/list/";
    }
}
