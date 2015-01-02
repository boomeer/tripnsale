var frDate = null;
var toDate = null;

function TextToDate(text)
{
    var val = text.match(/^(\d{2})\.(\d{2})\.(\d{4})$/);
    if (val) {
        return new Date(1*val[3], 1*val[2] - 1, 1*val[1]);
    } else {
        return null;
    }
}

function FromDateSelected(dateText, obj)
{
    frDate = TextToDate(dateText);
    if (frDate && toDate && frDate > toDate) {
        toDate = frDate;
        $("#inputToTime").datepicker("setDate", toDate);
    }
    $("#inputToTime").datepicker("option", "defaultDate", frDate);
}

function ToDateSelected(dateText, obj)
{
    toDate = TextToDate(dateText);
    if (frDate && toDate && frDate > toDate) {
        frDate = toDate;
        $("#inputFromTime").datepicker("setDate", frDate);
    }
    $("#inputFromTime").datepicker("option", "defaultDate", toDate);
}

$(function() {
    $.datepicker.setDefaults($.datepicker.regional['ru']);
    $("#inputFromTime").datepicker(
        {
            "dateFormat": "dd.mm.yy",
            "minDate": "-1m",
            "maxDate": "+3m",
            "onSelect": FromDateSelected
        });
    $("#inputToTime").datepicker(
        {
            "dateFormat": "dd.mm.yy",
            "minDate": "+1d",
            "maxDate": "+3m",
            "onSelect": ToDateSelected
        });

    CountriesAC($("#inputFrom"));
    CountriesAC($("#inputTo"));
});
