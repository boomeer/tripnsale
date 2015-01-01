function UsersGetPage()
{
    var found = window.location.hash.match(/^#userspage(\d+)$/);
    return (!found ? 1 : found[1]*1);
}

function UsersRefresh()
{
    $(".userList").html("Загрузка...");
    $.post("/user/filter/", {
        "page": UsersGetPage() - 1,
    }, function(res) {
        $(".userList").html(res);
    });
}

function UsersChangePage()
{
    if (window.location.hash.match(/^#userspage\d+$/)) {
        UsersRefresh();
    }
}

$(function() {
    $(window).bind('hashchange', UsersChangePage);
    UsersRefresh();
});
