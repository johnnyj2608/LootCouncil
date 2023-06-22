import pandas as pd
import pprint as pp
import requests
from bs4 import BeautifulSoup
import json
from auth import curl

'''
- Paste WCL Live Logs (input)
- Scrape WCL names
- Log into TMB
- Export Wishlist & Received
- Intersect WCL names w/ TMB
- Create Player dict, Value=[class, max(median/bracket) perf, received count]
- Intersect Contested TMB w/ items dict
- Hardcode Ulduar prio
- Contested dict: Item:[ [name1, rank], [name2, rank] ]
- Scores dict: Item: max(index + median + count + profile[player][2].index(item)
- Print pre-assigned items (scores)
- Multiple py files
- Dockerize
'''

received = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/received'
wishlist = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/wishlist'
#print(curl(wishlist))

sheet = '1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q'
physical_id = '594385335'
caster_id = '1620926651'

url = f'https://docs.google.com/spreadsheets/d/{sheet}/export?gid={physical_id}&format=csv'
df = pd.read_csv(url, skiprows=[0])
items = dict(zip(df['Item - Horde'], df['Prio']))

url = f'https://docs.google.com/spreadsheets/d/{sheet}/export?gid={caster_id}&format=csv'
df = pd.read_csv(url, skiprows=[0])
items.update(dict(zip(df['Item - Horde'], df['Prio'])))

# Need to hard-code Ulduar item and prio's here

#pp.pprint(items)

if __name__ == "__main__":
    print("Hello, World!")