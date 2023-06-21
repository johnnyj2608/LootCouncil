import pandas as pd

# Item, Prio = F, I

SHEET_ID = '1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q'
SHEET_NUMBER = '594385335'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?gid={SHEET_NUMBER}&format=csv'
df = pd.read_csv(url, skiprows=[0])
df = df[["Item - Horde", "Prio"]]

print(df)