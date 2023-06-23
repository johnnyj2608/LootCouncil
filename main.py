import pandas as pd
import pprint as pp
from bs4 import BeautifulSoup
from io import StringIO
from auth import curl
from wcl import get_names
from wcl import get_perf

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

    # Get raider name, class, and sort order
    response = curl(wishlist)
    csvStringIO = StringIO(response.text)
    df = pd.read_csv(csvStringIO, sep=",")
    df = df[df['received_at'].isnull()]

    prio = {k: f.groupby('character_name')['sort_order'].apply(list).to_dict()
     for k, f in df.groupby('item_name')}

    df = df[['character_name', 'character_class']].drop_duplicates()
    df = df.rename(columns={'character_class': 'Class'})
    raiders = df.set_index('character_name').T.to_dict()

    # Get raider received count (Unnecessary? Just count entries if NaN?)
    response = curl(received)
    csvStringIO = StringIO(response.text)
    df = pd.read_csv(csvStringIO, sep=",")
    df = df[['character_name']]
    df = df.groupby(df.columns.tolist(), as_index=False).size()
    temp = df.set_index('character_name').to_dict()['size']
    for key in raiders:
        try:
            raiders[key]['Received'] = temp[key]
        except:
            raiders[key]['Received'] = 0

    # Intersect today's raiders and get performance
    report_names = get_names(code='bPpcTmQrzGXdMxA6')
    raiders = {k: raiders[k] for k in report_names if k in raiders}
    for key in raiders:
        raiders[key].update(get_perf(name=key))

    # filter wishlist if didn't show up for raid

    for key in prio:
        score = float('inf')
        res = ''
        for name in prio[key]:
            cur = prio[key][name][0]
            cur += raiders[name]['Received']
            cur += wcl_perf(raiders[name]['Best'])
            cur += wcl_perf(raiders[name]['Med'])
            # parse items prio here
            if cur < score:
                score = cur
                res = name
        prio[key] = res
    print(prio)

def wcl_perf(perf):
    if perf > 95:
        return 1
    if perf > 75:
        return 2
    if perf > 50:
        return 3
    if perf > 25:
        return 4
    return 5

if __name__ == "__main__":
    main()