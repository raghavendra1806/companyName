#!/usr/bin/python3
import requests
import sys


def companyName():
    KEY = "at_DtI0mMoUs7qqiEk8q86iQeVsSLebR"

    MAC = sys.argv[1]
    URL = "https://api.macaddress.io/v1?apiKey=" +KEY+ "&output=json&search=" + MAC
    r = requests.get(url = URL)
    data = r.json()
    vendorName=data['vendorDetails']['companyName']
    if len(vendorName) == 0:
        print ("Vendor details doesn't exist for MAC Address " + MAC)
    else:
        print ("Company Name for MAC "+MAC+" : " + data['vendorDetails']['companyName'])

if __name__ == '__main__':
    companyName()
