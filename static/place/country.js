function CountriesFormat(item)
{
    return "<img src='/static/countries/" + item.id + "_preview.gif'>" + item.text;
}

function CountriesAC(el)
{
    $(el).select2({
        formatResult: CountriesFormat,
        formatSelection: CountriesFormat,
    });
}
