import pandas as pd
import pprint as pp
from bs4 import BeautifulSoup
from io import StringIO
from auth import curl
from wcl import get_names
from wcl import get_perf

def main():
    sheet = '1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q'

    # Physical spreadsheet prio
    physical_id = '594385335'
    url = f'https://docs.google.com/spreadsheets/d/{sheet}/export?gid={physical_id}&format=csv'
    df = pd.read_csv(url, skiprows=[0])
    df = df[['Item - Horde', 'Prio']]
    items = df.set_index('Item - Horde').to_dict()['Prio']

    # Caster spreadsheet prio
    caster_id = '1620926651'
    url = f'https://docs.google.com/spreadsheets/d/{sheet}/export?gid={caster_id}&format=csv'
    df = pd.read_csv(url, skiprows=[0])
    df = df[['Item - Horde', 'Prio']]
    items.update(df.set_index('Item - Horde').to_dict()['Prio'])

    # Ulduar specific prio
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


    # Create dict to store character info
    tmb = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/all'
    response = curl(tmb)
    csvStringIO = StringIO(response.text)
    df = pd.read_csv(csvStringIO, sep=",")
    wl = prio = df[df['type']=='wishlist']
    rd = df[df['type']=='received']

    # Gets name and class of character
    wl = wl[['character_name', 'character_class']].drop_duplicates()
    wl = wl.rename(columns={'character_class': 'Class'})
    raiders = wl.set_index('character_name').T.to_dict()

    # Gets received count of character
    rd = rd[['character_name']]
    rd = rd.groupby(rd.columns.tolist(), as_index=False).size()
    temp = rd.set_index('character_name').to_dict()['size']
    for key in raiders:
        try:
            raiders[key]['Received'] = temp[key]
        except:
            raiders[key]['Received'] = 0

    # Intersect today's raiders and get performance
    report_names = get_names(code='bPpcTmQrzGXdMxA6')
    raiders = {k: raiders[k] for k in raiders.keys() & report_names}
    for key in raiders:
        raiders[key].update(get_perf(name=key))

    # Need to ensure akka's isn't appended. Why is it float now?
    prio = {k: f.groupby('character_name')['sort_order'].apply(list).to_dict()
     for k, f in prio.groupby('item_name')}
    
    #pp.pprint(raiders)
    #pp.pprint(prio)
    #return

    for key in prio:
        score = float('inf')
        res = ''
        for name in prio[key]:
            cur = prio[key][name][0]
            cur += raiders[name]['Received']
            cur += perf_score(raiders[name]['Best'])
            cur += perf_score(raiders[name]['Med'])
            # parse items prio here
            if cur < score:
                score = cur
                res = name
        prio[key] = res
    pp.pprint(prio)

def perf_score(perf):
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