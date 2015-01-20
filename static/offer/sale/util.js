var gTripEditBackref;

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

function TripsRefresh(page)
{
    var sp = $("#tripsProfile");
    var so = $("#tripsOwner");
    var fr = $("#tripsFilterFrom");
    var to = $("#tripsFilterTo");
    var rec = $("#tripsRecommend");
    $(".tripsList").html("Загрузка...");
    $.post("/offer/sale/filter/", {
        "from": fr ? fr.val() : "",
        "to": to ? to.val() : "",
        "profile": sp ? sp.val() : 0,
        "page": (page ? page : TripsGetPage()),
        "owner": so ? so.val() : 0,
        "recommend": rec ? rec.val() : ""
    }, function(res) {
        $(".tripsList").html(res);
        $(".fast-profile-btn").click(StopPropagationEvent);
        $(".tripOwner.tripOwner-right.tripSection").click(StopPropagationEvent);
        $(".profileLink").click(StopPropagationEvent);
    });
}

function TripRefreshPage()
{
    TripsRefresh(TripsGetRealPage());
}

function TripCloseImpl(id, revert, refreshview /* = true */, refreshpage /* = true */)
{
    if (typeof refreshpage == "undefined") {
        refreshpage = true;
    }
    if (typeof refreshview == "undefined") {
        refreshview = true;
    }

    $.post("/offer/sale/close/", {
        "id": id,
        "revert": revert,
        "async": true
    }, function(res) {
        if (refreshpage) {
            TripRefreshView(id);
        }
        if (refreshview) {
            TripRefreshPage();
        }
    });
}

function TripClose(id, refreshview /* = true */, refreshpage /* = true */)
{
    TripCloseImpl(id, false, refreshview, refreshpage);
}

function TripReopen(id, refreshview /* = true */, refreshpage /* = true */)
{
    TripCloseImpl(id, true, refreshview, refreshpage);
}

function TripRefreshView(id, editBackref)
{
    if (editBackref) {
        editBackref = encodeURIComponent(editBackref);
        gTripEditBackref = editBackref;
    } else {
        editBackref = gTripEditBackref;
    }

    $(".tripViewContent").html("Загрузка...");
    $.ajax("/offer/sale/view/" + id, {
        "data": (editBackref ? { "editBackref": editBackref } : {}),
        "success": function(res) {
            $(".tripViewContent").html(res);
        },
        "error": function() {
            TripViewClose();
        },
    });

}

function TripView(id, notChangeHash, editBackref)
{
    if (!notChangeHash) {
        window.location.hash = "#trip" + id;
    }
    LockScroll();
    $(".tripViewWrapper").show();
    TripRefreshView(id, editBackref);
}

function TripViewClose(notChangeHash)
{
    if (!notChangeHash) {
        window.location.hash = "#tripspage" + TripsGetRealPage();
    }
    $(".tripViewWrapper").hide();
    $(".tripViewContent").html("");
    UnlockScroll();
}

function TripRemove(id)
{
    if (confirm("Вы действительно хотите удалить поездку?")) {
        var $tripViewContent = $(".tripViewContent");
        if ($tripViewContent) {
            $(".tripViewContent").html("Подождите, пожалуйста");
        }
        $.post("/offer/sale/remove/", {
            "id": id,
            "async": true
        }, function(res) {
            var $tripViewContent = $(".tripViewContent");
            if ($tripViewContent) {
                TripViewClose();
            }
            TripRefreshPage();
        });
    }
}
