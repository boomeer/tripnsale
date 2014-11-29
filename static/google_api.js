function AutoComplete(elId) {
    var autocomplete = new google.maps.places.Autocomplete(document.getElementById(elId), {
        language: 'ru',
        types: ['(cities)'],
    });
}
