import pandas as pd
import pprint as pp
import wcl
import time
from io import StringIO
from client import header

def main():
    items = {}
    spreadsheet = '1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q'
    sheet_ID = {'physical':'594385335', 'caster':'1620926651', 'tank':'1031043128'}
    for sheet in sheet_ID:
        res = spreadsheetPrio(spreadsheet, sheet_ID[sheet], items)
        if type(res) == int:
            return errorCodes(res)
    print('Retrieved spreadsheets')

    # Parse item priority string into lists
    for key in items:
        if type(items[key]) == float:   # Skipping NaN values
            continue
        temp = items[key].replace(' ', '').replace('>=', '>')
        temp = temp.split('>')
        for level in range(len(temp)):
            temp[level] = temp[level].split('=')
            for spec in range(len(temp[level])):
                cur = temp[level][spec].lower()
                if 'heal' in cur:
                    temp[level] = ['Holy', 'Restoration']
                elif 'dps' in cur:
                    temp[level] = ['Mage', 'Warlock', 'Shadow', 'Balance', 'Elemental']
                else:
                    temp[level][spec] = name_fix(temp[level][spec])
            if 'Rogue' in temp[level]:      # Split rogues into respective specs
                temp[level].remove('Rogue')
                temp[level].append('Combat')
                temp[level].append('Assassination')
            if 'Warlock' in temp[level]:      # Split warlock into respective specs
                temp[level].remove('Warlock')
                temp[level].append('Affliction')
                temp[level].append('Demonology')
        temp = [[x for x in sub_list if x] for sub_list in temp] # Remove empty strings
        items[key] = [x for x in temp if x != []] # Remove empty lists
    items['Greaves of Ruthless Judgment'] = items.pop('Greaves of the Ruthless Judgment') # Misspelled in spreadsheet
    print('Parsed spreadsheet')
    
    # Ulduar prio (for my guild specifically)
    items['Pharos Gloves'] = [['Fire', 'Arcane'], ['Affliction', 'Demonology'], ['Balance', 'Shadow'], ['Elemental']]
    items['Flare of the Heavens'] = [['Affliciton', 'Demonology'], ['Fire', 'Arcane'], ['Balance', 'Shadow', 'Elemental']]
    items['Conductive Seal'] = [['Affliciton', 'Demonology'], ['Fire', 'Arcane', 'Shadow', 'Balance', 'Elemental'], ['Holy', 'Resto']]
    items['Bindings of Winter Gale'] = [['Enhancement'], ['Elemental'], ['Resto'], ['Holy']]
    items['Scale of Fates'] = [['Affliction', 'Demonology'], ['Balance', 'Shadow'], ['Fire', 'Arcane']]
    items["Comet's Trail"] = [['Rogue', 'Enhancement', 'Unholy']]

    items['Seal of the Betrayed King'] = [['Frost']]
    items['Sabatons of Lifeless Night'] = [['Unholy']]
    items['Armbands of Bedlam'] = [['Unholy']]
    items['Frigid Strength of Hodir'] = [['Frost']]
    items['Crown of Luminescence'] = [['Holy']]

    # Create dict to store character info
    tmb = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/all'
    response = header(tmb)
    if type(response) == int:
        return errorCodes(response)
    csvStringIO = StringIO(response.text)
    df = pd.read_csv(csvStringIO, sep=",")
    wl = prio = df[(df['type']=='wishlist') & (df['received_at'].isnull())]
    rd = df[(df['type']=='received') & (df['received_at'].notnull())]

    # Gets character name and received count
    wl = wl[['character_name']].drop_duplicates()
    raiders = wl.set_index('character_name').T.to_dict()
    rd = rd[['character_name']]
    rd = rd.groupby(rd.columns.tolist(), as_index=False).size()
    temp = rd.set_index('character_name').to_dict()['size']
    for key in raiders:
        try:
            raiders[key]['Received'] = temp[key]
        except:
            raiders[key]['Received'] = 0
    print('Created player information')

    # Intersect report's attendance with raider dict and get performance & spec
    report = input("What's the report link? ") or "bPpcTmQrzGXdMxA6"
    if '/' in report:
        report = report.split('/')[4]
    report_names = wcl.get_names(code=report)
    if type(report_names) == int:
        return errorCodes(report_names)
    report_names = set(report_names)
    print('Retrieved names from report')

    delete_keys = []
    for key in raiders:
        if key in report_names:
            cur = wcl.get_perf(name=key)
            if type(cur) == int:
                return errorCodes(cur)
            raiders[key].update(wcl.get_perf(name=key))
        else:
            delete_keys.append(key)
            prio = prio[prio['character_name'] != key]
    for key in delete_keys:
        del raiders[key]
    print('Updated eligible players with performance metric')

    # Create prio dictionary, {item_name:{character_name:[sort_order]}
    prio = {k: f.groupby('character_name')['sort_order'].apply(list).to_dict()
     for k, f in prio.groupby('item_name')}
    for key in prio:
        prio[key].update({'Prio':items[key]})
    print('Created item to player map')

     # Calculate values and assign highest priority name(s) to item
    for key in prio:
        score = float('inf')
        res = []
        for name in prio[key]:
            if name == 'Prio':
                continue
            cur = int(prio[key][name][0])    # sort order
            cur += raiders[name]['Received']
            cur += perf_score(raiders[name]['Best'])
            cur += perf_score(raiders[name]['Med'])

            for i in range(len(prio[key]['Prio'])):
                if raiders[name]['Spec'] not in prio[key]['Prio'][i]:
                    cur += 1
                else:
                    break
            if cur < score:
                score = cur
                res = [name]
            elif cur == score:
                res.append(name)
        prio[key] = res
    print('Assigned priority to items')
    return prio

def perf_score(perf):
    """
    perf_score converts performance numbers to a point system
    :param perf: int, performance value 0-100 to be converted
    :return: the point system value
    """ 
    if perf > 95:
        return 0
    elif perf > 75:
        return 1
    elif perf > 50:
        return 2
    elif perf > 25:
        return 3
    return 4

def name_fix(spec):
    """
    name_fix changes inconsistencies in names in spreadsheet
    :param spec: str, the spec name to be changed to be consistent
    :return: the consistent spec/class name
    """ 
    spec = spec.lower()
    if 'warr' in spec or 'w' == spec:
        return 'Warrior'
    elif 'ret' in spec:
        return 'Retribution'
    elif 'tp' in spec or 'pp' in spec:
        return 'Paladin'
    elif 'uh' in spec or 'unholy' in spec:
        return 'Unholy'
    elif 'fr' in spec or 'f' == spec or 'fd' == spec:
        return 'Frost'
    elif 'blood' in spec or 'dk' == spec:
        return 'Blood'
    elif 'hunt' in spec or 'h' == spec:
        return 'Hunter'
    elif 'enh' in spec:
        return 'Enhancement'
    elif 'ele' in spec:
        return 'Elemental'
    elif 'combat' in spec:
        return 'Combat'
    elif 'assassination' in spec:
        return 'Assassination'
    elif 'rog' in spec or 'r' == spec:
        return 'Rogue'
    elif 'feral' in spec:
        return 'Feral'
    elif 'boom' in spec:
        return 'Balance'
    elif 'demo' in spec:
        return 'Demonology'
    elif 'aff' in spec:
        return 'Affliction'
    elif 'lock' in spec:
        return 'Warlock'
    elif 'mage' in spec or 'arcane' in spec or 'fire' in spec:
        return 'Mage'
    elif 'sp' in spec:
        return 'Shadow'
    elif 'pri' in spec or 'disc' in spec or 'yp' in spec or 'hp' in spec:
        return 'Holy'
    elif 'rsh' in spec or 'osh' in spec or 'rdr' in spec or 'sham' in spec:
        return 'Restoration'
    else:
        return ''
    
def spreadsheetPrio(spreadsheet, sheet, priority):
    """
    imports a spreadsheet about prio into a dictionary
    :param spreadsheet: str, the spreadsheet link
    :param sheet: str, the sheet link
    :param spreadsheet: dict, the dictionary to store prios
    :return: dictionary of item to class prio
    """ 
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet}/export?gid={sheet}&format=csv'
    try:
        df = pd.read_csv(url, skiprows=[0])
    except:
        return 2
    df = df[['Item - Horde', 'Prio']]
    priority.update(df.set_index('Item - Horde').to_dict()['Prio'])
    return

def errorCodes(number):
    res = 'Error: '
    if number == 0:
        return 'Not a valid report code'
    elif number == 1:
        return 'Not a valid WCL profile name'
    elif number == 2:
        return 'Not a valid spreadsheet'
    elif number == 3:
        return 'Not a valid wishlist'

if __name__ == "__main__":
    start_time = time.time()
    res = main()
    if type(res) == str:
        print(res)
    else:
        with open("Output.txt", "w") as text_file:
            text_file.write(pp.pformat(res))
    print("Process finished --- %s seconds ---" % (time.time() - start_time))