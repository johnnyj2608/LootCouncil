import pandas as pd
import pprint as pp
from bs4 import BeautifulSoup
from io import StringIO
from clientkey import clientkey
from auth import curl

def main():
    sheet = '1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q'
    
    physical_id = '594385335'
    url = f'https://docs.google.com/spreadsheets/d/{sheet}/export?gid={physical_id}&format=csv'
    df = pd.read_csv(url, skiprows=[0])
    df = df[['Item - Horde', 'Prio']]
    items = df.set_index('Item - Horde').to_dict()['Prio']

    caster_id = '1620926651'
    url = f'https://docs.google.com/spreadsheets/d/{sheet}/export?gid={caster_id}&format=csv'
    df = pd.read_csv(url, skiprows=[0])
    df = df[['Item - Horde', 'Prio']]
    items.update(df.set_index('Item - Horde').to_dict()['Prio'])

    items['Pharos Gloves'] = 'Fire > Lock > Boomy/Spriest > Ele'
    items['Flare of the Heavens'] = 'Demo > Fire/Aff > Boom/Spriest/Ele'
    items['Conductive Seal'] = 'Demo > Caster DPS > Healers'
    items['Bindings of Winter Gale'] = 'Enh > Ele > Rshaman > Hpal'
    items['Scale of Fates'] = 'Aff > Boomy/Spriest > Mage'
    items["Comet's Trail"] = 'Rogue=Enh=UH>all'

    items['Seal of the Betrayed King'] = 'Frost DK'
    items['Sabatons of Lifeless Night'] = 'UH Dk'
    items['Armbands of Bedlam'] = 'UH Dk'
    items['Frigid Strength of Hodir'] = 'Frost Dk'
    items['Crown of Luminescence'] = 'Priest'
   

    wishlist = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/wishlist'
    received = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/received'

    # Get raider name and class
    response = curl(wishlist)
    csvStringIO = StringIO(response)
    df = pd.read_csv(csvStringIO, sep=",")
    df = df[['character_name', 'character_class']].drop_duplicates()
    raiders = df.set_index('character_name').T.to_dict('list')

    # Get raider received count
    response = curl(received)
    csvStringIO = StringIO(response)
    df = pd.read_csv(csvStringIO, sep=",")
    df = df[['character_name']]
    df = df.groupby(df.columns.tolist(), as_index=False).size()
    temp = df.set_index('character_name').to_dict()['size']
    for key in raiders:
        try:
            raiders[key].append(temp[key])
        except:
            raiders[key].append(0)

    # Scrape WCL and intersect names. Then get max(median/bracket) perf
    print(clientkey())

if __name__ == "__main__":
    main()