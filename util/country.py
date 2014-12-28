#!/usr/bin/env python
import lxml.html
from place.models import Country


def Parse(data):
    doc = lxml.html.document_fromstring(data)
    for tr in doc.cssselect("table.country tr")[2:]:
        name = "_".join(tr[0][0][0].get("src").split("/")[-1].split(".")[0].split("_")[:-1])
        title = tr[1][0].text
        c = Country.objects.filter(name=name).all()
        if not c:
            print(name)
            country = Country(
                name=name,
                title=title,
                order=0
            )
            country.save()
    orders = {
        "russia": 100,
        "united_states_of_america": 80,
        "european_union": 60,
    }
    for c in orders:
        country = Country.objects.get(name=c)
        country.order = orders[c]
        country.save()
        print(country.name, "set order to", country.order)
    


def Main(args=None):
    with open("util/countries.html", "r", encoding="utf-8") as f:
        data = f.read()
        Parse(data)


if __name__  == "__main__":
    Main()
