#!/usr/bin/env python
import lxml.html
from place.models import Country


def Parse(data):
    doc = lxml.html.document_fromstring(data)
    for tr in doc.cssselect("table.country tr")[2:]:
        name = "_".join(tr[0][0][0].get("src").split("/")[-1].split(".")[0].split("_")[:-1])
        title = tr[1][0].text
        print(name, title)
        country = Country(
            name=name,
            title=title,
        )
        country.save()


def Main(args=None):
    with open("util/countries.html", "r") as f:
        data = f.read()
        Parse(data)


if __name__  == "__main__":
    Main()
