$(function() {
    $.datepicker.setDefaults($.datepicker.regional['ru']);
    $("#inputBday").datepicker(
        {
            "dateFormat": "dd.mm.yy",
            "maxDate": "-16y",
            "changeYear": true,
            "changeMonth": true
        });
    CountriesAC("#inputCountry");
});
