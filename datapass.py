#!/usr/bin/env python3
import requests
import urllib.request

url = "http://datapass.de/api/service/generic/v1/status"

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",

}
response = requests.get(url, headers=headers)
js = response.json()

#print(js)

print(js["title"] + ": ")
if "usedPercentage" in js:
    if js["usedPercentage"] == 100:
        print("\tInkludiertes Datenvolumen mit hoher Geschwindigkeit verbraucht")
        print("\tVerbleibende Zeit: " + js["remainingTimeStr"])
        print("\tSubscriptions: " + str(js["subscriptions"]))

    else:
        print("\tTarif: " + js["passName"])
        print("\tDatenvolumen: " + js["initialVolumeStr"])
        print("\tVerbraucht: " + js["usedVolumeStr"] + " (" + str(js["usedPercentage"]) + "%)")


# if "usedVolumeStr" in js:
#     print(js["usedVolumeStr"])
#
#     print(js["usedVolumeStr"] + "/" + js["initialVolumeStr"] + " => " +
#           str(js["usedPercentage"]) + "%. Restlaufzeit: " + js["remainingTimeStr"] + " - Tarif: " + js["passName"])
#     if js["hasOffers"]:
#         print("Ein Angebot liegt vor!")
