function ClearDate() {
    $("#inputBday").datepicker("setDate", "");
}

$(function() {
    $.datepicker.setDefaults($.datepicker.regional['ru']);
    $("#inputBday").datepicker(
        {
            "dateFormat": "dd.mm.yy",
            "changeYear": true,
            "showOtherMonths": true,
            "selectOtherMonths": true,
            "changeMonth": true
        });
    CountriesAC("#inputCountry");
});
