#!/usr/bin/env python

import xml.etree.ElementTree as xmltree
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from valute.models import Valute
from datetime import datetime

def UpdateRates(url="http://www.cbr.ru/scripts/XML_daily.asp", force=False):
    response = urlopen(url)

    text = response.read().decode('cp1251')
    curTime = datetime.now()
    cbr = xmltree.fromstring(text)
    updDate = datetime.strptime(cbr.get("Date"), "%d.%m.%Y").date()
    print ("now is {}, xml updated at {}.".format(curTime, updDate))

    if len(Valute.objects.all()):
        latestInBase = Valute.objects.all()[0]
        if latestInBase.date == updDate:
            print ("\tThe latest data in base.")
            if not force:
                print ("")
                return

    for valute in cbr.findall('Valute'):
        print ("\t{name}->RUB: {nominal}->{value}".format(
                name=valute.find("CharCode").text,
                nominal=float(valute.find("Nominal").text.replace(',', '.')),
                value=float(valute.find("Value").text.replace(',', '.'))))
        v = Valute(
            date=updDate,
            updTime=curTime,
            fromVal=float(valute.find("Nominal").text.replace(',', '.')),
            fromName=valute.find("Name").text,
            fromId=valute.find("CharCode").text,
            toVal=float(valute.find("Value").text.replace(',', '.')))
        v.save()

    print ("")

if __name__ == "__main__":
    UpdateRates()
