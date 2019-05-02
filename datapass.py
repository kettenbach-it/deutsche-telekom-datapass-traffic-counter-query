#!/usr/bin/env python3
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://datapass.de/home?continue=true"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find("div", class_="barTextBelow").text
billingPeriod = soup.find("td", class_="infoValue billingPeriod").text
remainingTime = soup.find("td", class_="infoValue remainingTime").text

print("Abrechnungsmonat: " + billingPeriod)
print(data)
print("Restzeit: " + remainingTime)