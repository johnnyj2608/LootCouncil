import pandas as pd
import pprint as pp
import requests
from bs4 import BeautifulSoup
import json
from auth import curl

def main():
    received = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/received'
    wishlist = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/wishlist'
    #print(curl(wishlist))

    sheet = 
    physical_id = '594385335'
    caster_id = '1620926651'

    url = f'https://docs.google.com/spreadsheets/d/1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q/export?gid={physical_id}&format=csv'
    df = pd.read_csv(url, skiprows=[0])
    items = dict(zip(df['Item - Horde'], df['Prio']))

    url = f'https://docs.google.com/spreadsheets/d/1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q/export?gid={caster_id}&format=csv'
    df = pd.read_csv(url, skiprows=[0])
    items.update(dict(zip(df['Item - Horde'], df['Prio'])))

    # Hard-code Ulduar item and prio's here
    #pp.pprint(items)

if __name__ == "__main__":
    main()