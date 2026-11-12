import pandas as pd

filepath = 'files/nilaiKuliah.csv'

df_csv = pd.read_csv(filepath,delimiter=",",encoding="latin1")
print(df_csv.head(2))