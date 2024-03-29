spreadsheet = '1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q'

sheetID = {'physical':'594385335', 'caster':'1620926651', 'tank':'1031043128'}

tmb = 'https://thatsmybis.com/15596/raid-team-two/export/loot/html/all'

guildID = 695278

# Ulduar prio (for my guild specifically)
def update_prio(items):
    items['Pharos Gloves'] = [['Fire', 'Arcane'], ['Affliction', 'Demonology'], ['Balance', 'Shadow'], ['Elemental']]
    items['Flare of the Heavens'] = [['Affliciton', 'Demonology'], ['Fire', 'Arcane'], ['Balance', 'Shadow', 'Elemental']]
    items['Conductive Seal'] = [['Affliciton', 'Demonology'], ['Fire', 'Arcane', 'Shadow', 'Balance', 'Elemental'], ['Holy', 'Resto']]
    items['Bindings of Winter Gale'] = [['Enhancement'], ['Elemental'], ['Resto'], ['Holy']]
    items['Scale of Fates'] = [['Affliction', 'Demonology'], ['Balance', 'Shadow'], ['Fire', 'Arcane']]
    items["Comet's Trail"] = [['Rogue', 'Enhancement', 'Unholy']]

    items['Seal of the Betrayed King'] = [['Frost']]
    items['Sabatons of Lifeless Night'] = [['Unholy']]
    items['Crown of Luminescence'] = [['Holy']]
    items['Frigid Strength of Hodir'] = [['Frost']]

    items['Greaves of Ruthless Judgment'] = items.pop('Greaves of the Ruthless Judgment') # Misspelled in spreadsheet
    return items