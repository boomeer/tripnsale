#-*- coding:utf-8 -*-
from django import template

register = template.Library()

@register.filter
def convertvalute(value, course):
    return float(value)*course.toVal/course.fromVal

@register.filter
def valuteround(value, prec=3):
    return int(round(float(value)/10**prec))*10**prec

@register.filter
def valutesub(first, second):
    return abs(float(first) - float(second))

@register.filter
def valuteperc(val, perc):
    return float(val)*perc

@register.filter
def textthousands(value, lang="ru"):
    thtext = "thousands"
    thval = int(round(float(value)/10**3))
    if lang == "ru":
        lastdig = int(str(thval)[-1])
        if lastdig == 1:
            thtext = "тысяча"
        elif lastdig >= 2 and lastdig <= 4:
            thtext = "тысячи"
        else:
            thtext = "тысяч"

    return "{num} {text}".format(num=thval, text=thtext)


