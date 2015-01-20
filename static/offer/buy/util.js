var gBuyEditBackref;

function BuyGetPage(defultPage)
{
    if (typeof defaultPage == "undefined") {
        defaultPage = 1;
    }
    var found = window.location.hash.match(/^#buyspage(\d+)$/);
    return (!found ? defaultPage : found[1]*1);
}

function BuyGetRealPage()
{
    return $("#buysPage").val();
}

function BuysRefresh(page)
{
    var bp = $("#buysProfile");
    var bo = $("#buysOwner");
    var fr = $("#buysFilterFrom");
    var to = $("#buysFilterTo");
    var rec = $("#buysRecommend");
    $(".buysList").html("Загрузка...");
    $.post("/offer/buy/filter/", {
        "title": $("#buysTitle").val(),
        "fr": fr ? fr.val() : "",
        "to": to ? to.val() : "",
        "profile": bp ? bp.val() : "",
        "recommend": rec ? rec.val() : "",
        "page": (page ? page : BuyGetPage()),
        "owner": bo ? bo.val() : 0,
    }, function(res) {
        $(".buysList").html(res);
        $(".owner.owner-right.buy-section").click(StopPropagationEvent);
        $(".profile-link").click(StopPropagationEvent);
        $(".fast-profile-btn").click(StopPropagationEvent);
    });
}

function BuysRefreshPage()
{
    BuysRefresh(BuyGetRealPage());
}


function BuyCloseImpl(id, revert, refreshview /* = true */, refreshpage /* = true */)
{
    if (typeof refreshpage == "undefined") {
        refreshpage = true;
    }
    if (typeof refreshview == "undefined") {
        refreshview = true;
    }

    $.post("/offer/buy/close/", {
        "id": id,
        "revert": revert,
        "async": true
    }, function(res) {
        if (refreshpage) {
            BuyRefreshView(id);
        }
        if (refreshview) {
            BuysRefreshPage();
        }
    });
}

function BuyClose(id, refreshview /* = true */, refreshpage /* = true */)
{
    BuyCloseImpl(id, 0, refreshview, refreshpage);
}

function BuyReopen(id, refreshview /* = true */, refreshpage /* = true */)
{
    BuyCloseImpl(id, 1, refreshview, refreshpage);
}

function BuyRefreshView(id, editBackref)
{
    console.log(editBackref);
    if (editBackref) {
        editBackref = encodeURIComponent(editBackref);
        gBuyEditBackref = editBackref;
    } else {
        editBackref = gBuyEditBackref;
    }

    console.log(editBackref, (editBackref ? "123" : "321"));
    $(".buyViewContent").html("Загрузка...");
    $.ajax("/offer/buy/view/" + id, {
        "data": (editBackref ? { "editBackref": editBackref } : {}),
        "success": function(res) {
            $(".buyViewContent").html(res);
        },
        "error": function() {
            BuyViewClose();
        },
    });
}

function BuyView(id, notChangeHash, editBackref)
{
    if (!notChangeHash) {
        window.location.hash = "#buy" + id;
    }
    LockScroll();
    $(".buyViewWrapper").show();
    BuyRefreshView(id, editBackref);
}

function BuyRemove(id)
{
    if (confirm("Вы действительно хотите удалить заказ?")) {
        var $buyViewContent = $(".buyViewContent");
        if ($buyViewContent) {
            $(".buyViewContent").html("Подождите, пожалуйста");
        }
        $.post("/offer/buy/remove/", {
            "id": id,
            "async": true
        }, function(res) {
            var $buyViewContent = $(".buyViewContent");
            if ($buyViewContent) {
                BuyViewClose();
            }
            BuysRefreshPage();
        });
    }
}

function BuyViewClose(notChangeHash)
{
    if (!notChangeHash) {
        window.location.hash = "#buyspage" + BuyGetRealPage();
    }
    $(".buyViewWrapper").hide();
    $(".buyViewContent").html("");
    UnlockScroll();
}
