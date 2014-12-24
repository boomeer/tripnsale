$(function() {
    $("#inputFromTime").datepicker({
        dateFormat: "dd.mm.yy",
    });
    $("#inputToTime").datepicker({
        dateFormat: "dd.mm.yy",
    });

    CountriesAC($("#inputFrom"));
    CountriesAC($("#inputTo"));
});
