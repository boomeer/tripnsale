$(function() {
    $(".userLoginBtn").on("click", function() {
        $(".userLoginForm").toggle();
    });

    $(".userLoginFormHideBtn").on("click", function() {
        $(".userLoginForm").hide();
    });
});
