# This program print out the dates of the bank holidays that happen in Northern Ireland
# and then print out excluding the bh celebrated in other parts of UK
# This program use the next Url with JSON data:
# https://www.gov.uk/bank-holidays.json
# Author: Tanya San Juan

# We can use requests module instead to import Jason
# to request to a website the data in study.
# source: https://www.w3schools.com/python/module_requests.asp

import requests
url = 'https://www.gov.uk/bank-holidays.json'
response = requests.get(url)
data = response.json()
for bh in data ['northern-ireland']['events']:
    print(f'{bh['title']} is on {bh['date']}')
# this print all the bank holidays happen in Northern Ireland, from 2024 until 2027. 
# A total of 10 festivities during the year.


# Program modified to get only the BH celebrated in NI, excluding the rest of UK
ni_bankholidays = data['northern-ireland']['events']

for bh in ni_bankholidays:
    if bh not in data ['england-and-wales']['events'] and bh not in data['scotland']['events']:
        print (f'{bh['title']} is on {bh['date']}')

# This prints two festivities: St. Patrick's day and Orangemen's day. 
# From 2024 until 2027
