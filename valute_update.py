#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
import util.valute
import argparse
import sys
from datetime import (datetime, time, date, timedelta)
from time import sleep

def run():
    util.valute.UpdateRates()


def main(argv):
    if not argv.daemon:
        run()
        return

    pdate = datetime.now().date()
    runtime = sorted(argv.time)

    rtind = 0
    while rtind < len(runtime) and runtime[rtind] < datetime.now().time():
        rtind += 1
    if rtind == len(runtime):
        rtind = 0

    intv = 0 if argv.interval else -1

    while True:
        runned = False
        def runonce(runned):
            if not runned:
                run()
            return True
        ctime = datetime.now().time()
        cdate = datetime.now().date()

        if intv == 0:
            print("int")
            runned = runonce(runned)
            intv = argv.interval
        if intv > 0:
            intv -= 1

        if pdate != cdate:
            while rtind < len(runtime):
                runned = runonce(runned)
                rtind += 1
            rtind = 0
        while rtind < len(runtime) and runtime[rtind] < datetime.now().time():
            runned = runonce(runned)
            rtind += 1

        pdate = cdate
        sleep(60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--daemon", dest="daemon", action="store_true", default=False,
                        help="if set, scrip will be running in loop.")
    parser.add_argument("-t", "--time", dest="time", action="append",
                        help="time for running the daemon. could be set multiple times. "
                             "default is [ 00:00 ]. if --daemon wasn't set, option "
                             "will be ignored")
    parser.add_argument("-i", "--interval", dest="interval", metavar="minutes", type=int,
                        default=None, help="if set, the daemon will run with given interval. "
                                           "if --daemon wasn't set, option will be ignored")
    argv = parser.parse_args()
    if not argv.time:
        argv.time = [ time() ]
    else:
        argv.time = [ datetime.strptime(val, "%H:%M").time() for val in argv.time ]
    argv.time = list(set(argv.time))

    main(argv)
