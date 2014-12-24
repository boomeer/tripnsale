#!/usr/bin/env python

import xml.etree.ElementTree as xmltree
import urllib.request
from valute.models import Valute
from datetime import datetime

def UpdateRates(url="http://www.cbr.ru/scripts/XML_daily.asp"):
    response = urllib.request.urlopen(url)

    text = response.read().decode('cp1251')
    curTime = datetime.now()
    cbr = xmltree.fromstring(text)
    updDate = datetime.strptime(cbr.get("Date"), "%d.%m.%Y")
    for valute in cbr.findall('Valute'):
        v = Valute(
            date=updDate,
            updTime=curTime,
            fromVal=float(valute.find("Nominal").text.replace(',', '.')),
            fromName=valute.find("Name").text,
            fromId=valute.find("CharCode").text,
            toVal=float(valute.find("Value").text.replace(',', '.')))
        v.save()

if __name__ == "__main__":
    UpdateRates()
