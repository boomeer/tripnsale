from django.shortcuts import HttpResponse


class TsExc(Exception):
    pass


def SafeViewFunc(func, *arg, **argv):
    try:
        return func(*arg, **argv)
    except Exception as e:
        return HttpResponse("Error: {}".format(e))


def SafeView(func):
    return lambda *arg, **argv: SafeViewFunc(func, *arg, **argv)

