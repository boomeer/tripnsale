$(function() {
    CountriesAC("#inputCountry");
    $("#offert-check").change(function() {
        if (this.checked) {
            $("#reg-btn").removeAttr("disabled");
        } else {
            $("#reg-btn").attr("disabled", "1");
        }
    });
});
