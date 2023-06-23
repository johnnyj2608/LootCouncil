import pandas as pd
import pprint as pp
from bs4 import BeautifulSoup
from io import StringIO
from auth import curl
from wcl import get_names
from wcl import get_perf

def perf_score(perf):
    if perf > 95:
        return 0
    if perf > 75:
        return 1
    if perf > 50:
        return 2
    if perf > 25:
        return 3
    return 4

def class_prio(item, spec):
    print(item, spec)
    return

def name_fix(spec):
    spec = spec.lower()
    if 'combat' in spec:
        return 'Combat'
    elif 'assassination' in spec:
        return 'Assassination'
    elif 'feral' in spec:
        return 'Feral'
    elif 'ret' in spec:
        return 'Retribution'
    elif 'pal' in spec:
        return 'Paladin'
    elif 'dk' in spec:
        return 'Death Knight'
    elif 'blood' in spec:
        return 'Blood'
    elif 'uh' in spec or 'unholy' in spec:
        return 'Unholy'
    elif 'fr' in spec or 'f' == spec:
        return 'Frost'
    elif 'enh' in spec:
        return 'Enhancement'
    elif 'rog' in spec or 'r' == spec:
        return 'Rogue'
    elif 'warr' in spec or 'w' == spec:
        return 'Warrior'
    elif 'hunt' in spec or 'h' == spec:
        return 'Hunter'
    elif 'lock' in spec or 'aff' in spec or 'demo' in spec:
        return 'Warlock'
    elif 'mage' in spec or 'arcane' in spec or 'fire' in spec:
        return 'Mage'
    elif 'boom' in spec:
        return 'Balance'
    elif 'rs' in spec or 'os' in spec:
        return 'Resto Shaman'
    elif 'ele' in spec or 'sham' in spec:
        return 'Elemental'
    elif 'rd' in spec:
        return 'Resto Druid'
    elif 'sp' in spec:
        return 'Shadow'
    elif 'pr' in spec:
        return 'Priest'
    elif 'yp' in spec:
        return 'Holy Paladin'
    elif 'disc' in spec:
        return 'Discipline'
    elif 'resto' in spec or 'heal' in spec:
        return 'Healer'
    elif 'dps' in spec:
        return 'DPS'
    elif 'tank' in spec:
        return 'Tank'
    else:
        return ''

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

    # Tank spreadsheet prio
    tank_id = '1031043128'
    url = f'https://docs.google.com/spreadsheets/d/{sheet}/export?gid={tank_id}&format=csv'
    df = pd.read_csv(url, skiprows=[0])
    df = df[['Item - Horde', 'Prio']]
    items.update(df.set_index('Item - Horde').to_dict()['Prio'])

    # Parse item priority string into lists
    for key in items:
        if type(items[key]) == float:   # Removing NaN values
            continue
        temp = items[key].replace(' ', '').replace('>=', '>')
        temp = temp.split('>')
        for i in range(len(temp)):
            temp[i] = temp[i].split('=')
            for j in range(len(temp[i])):
                temp[i][j] = name_fix(temp[i][j])
        items[key] = temp
    items['Greaves of Ruthless Judgment'] = items.pop('Greaves of the Ruthless Judgment') # Misspelled in spreadsheet
    pp.pprint(items)
    return
    # Remove non class names (pumper, rest)
    # Convert class abbreviations to full name
    # Non-spec classes: Warrior/Hunter

    # Ulduar prio (for my guild specifically)
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
    wl = prio = df[(df['type']=='wishlist') & (df['received_at'].isnull())]
    rd = df[(df['type']=='received') & (df['received_at'].notnull())]

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

    # Intersect report's attendance with raider dict and get performance
    report_names = set(get_names(code='bPpcTmQrzGXdMxA6'))
    delete_keys = []
    for key in raiders:
        if key in report_names:
            raiders[key].update(get_perf(name=key))
        else:
            delete_keys.append(key)
            prio = prio[prio['character_name'] != key]
    for key in delete_keys:
        del raiders[key]

    # Create prio dictionary, {item_name:{character_name:[sort_order]}
    prio = {k: f.groupby('character_name')['sort_order'].apply(list).to_dict()
     for k, f in prio.groupby('item_name')}
    for key in prio:
        print(prio[key], items[key])
        prio[key].update({'Prio':items[key]})
    pp.pprint(prio)
    return

    # Calculate values and assign one name to item
    for key in prio:
        score = float('inf')
        res = ''
        for name in prio[key]:
            cur = int(prio[key][name][0])    # sort order
            cur += raiders[name]['Received']
            cur += perf_score(raiders[name]['Best'])
            cur += perf_score(raiders[name]['Med'])
            cur += class_prio(key, raiders[name]['Class']) # Change to spec. Convert to appropriate name in function
            if cur < score:
                score = cur
                res = name
        prio[key] = (res, 'Rank: '+str(score))
    pp.pprint(prio)

if __name__ == "__main__":
    main()