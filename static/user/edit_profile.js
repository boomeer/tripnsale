$(function() {
    alert("123");
    $("#inputBday").datepicker();
    $("#inputBday").datepicker("option", "dateFormat", "dd.mm.yy");

    CountriesAC("#inputCountry");
});
