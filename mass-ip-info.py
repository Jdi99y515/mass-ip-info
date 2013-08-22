#!/usr/bin/env python
# encoding: utf-8
"""
Starter_Script_With_Args.py

Created by Scott Roberts.
Copyright (c) 2013 TogaFoamParty Studios. All rights reserved.
"""

import sys
import csv
from pygeocoder import Geocoder
import socket


# Setup Text Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def main():
    arg = sys.argv[1]

    print "Loading " + arg

    with open(arg, 'rb') as sourcefile:
        print "Parsing CSV"
        ddosers = sourcefile.readlines()

        outfile = open('ips-info.csv', 'wb')
        writer = csv.writer(outfile, dialect='excel')

        for ip in ddosers:
            ip = ip.strip()
            print "Analyzing: " + ip

            try:
              geoinfo =  Geocoder.geocode(ip)[0]
              geo_full = str(geoinfo)
              geo_country = str(geoinfo.country)
            except:
              geo_full = "-"
              geo_country = "-"

            try:
              hostinfo = socket.gethostbyaddr(ip)[0]
            except socket.herror as e:
              hostinfo = '-'
            except:
              hostinfo = '-'

            hoststring = [ip, geo_full, geo_country, str(hostinfo)]

            writer.writerow(hoststring)

    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "User aborted."
    except SystemExit:
        raise
    except:
        raise
