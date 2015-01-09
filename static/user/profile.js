function CloseAll()
{
    BuyViewClose(true);
    TripViewClose(true);
}

function OnHashChange()
{
    if (window.location.hash.match(/^#buyspage\d+$/)) {
        CloseAll()
        if (BuyGetPage() != BuyGetRealPage()) {
            BuysRefresh();
        }
    } else if (window.location.hash.match(/^#buy\d+$/)) {
        TripViewClose(true);
        BuyView(window.location.hash.slice(4), true);
    } else if (window.location.hash.match(/^#tripspage\d+$/)) {
        CloseAll();
        if (TripsGetPage() != TripsGetRealPage()) {
            TripsRefresh();
        }
    } else if (window.location.hash.match(/^#trip\d+$/)) {
        BuyViewClose(true);
        TripView(window.location.hash.slice(5), true);
    } else {
        CloseAll();
    }
}

$(function() {
    BuysRefresh();
    TripsRefresh();
    $(window).bind('hashchange', OnHashChange);
    OnHashChange();
});
