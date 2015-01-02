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

function FromDateHightlight(date)
{
    return [ true, (date - toDate == 0 ? "ui-state-highlight2" : ""), "" ];
}

function ToDateHightlight(date)
{
    return [ true, (date - frDate == 0 ? "ui-state-highlight2" : ""), "" ];
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
            "showOtherMonths": true,
            "selectOtherMonths": true,
            "onSelect": FromDateSelected,
            "beforeShowDay": FromDateHightlight
        });
    $("#inputToTime").datepicker(
        {
            "dateFormat": "dd.mm.yy",
            "minDate": "+1d",
            "showOtherMonths": true,
            "selectOtherMonths": true,
            "onSelect": ToDateSelected,
            "beforeShowDay": ToDateHightlight
        });

    CountriesAC($("#inputFrom"));
    CountriesAC($("#inputTo"));
});
