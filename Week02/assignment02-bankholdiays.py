# This program print out the dates of the bank holidays that happen in Northern Ireland
# excluding the bh celebrated in other parts of UK
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
ni_bankholidays = data['northern-ireland']['events']

for bh in ni_bankholidays:
    if bh not in data ['england-and-wales']['events'] and bh not in data['scotland']['events']:
        print (f'{bh['title']} is on {bh['date']}')

# This prints two festivities: St. Patrick's day and Orangemen's day. 
# From 2024 until 2027