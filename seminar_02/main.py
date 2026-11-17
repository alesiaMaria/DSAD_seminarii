import os

import pandas as pd
from scipy.spatial.distance import cdist

from functii_online import nan_replace_df, salvare_matrice

os.makedirs('data_out', exist_ok=True)


#Cerinta 1
df=pd.read_csv('winequality-red.csv', sep=';')

print("Shape (numarul de linii si coloane)", df.shape)
print("\n Primele 5 randuri de date sunt : ")
print(df.head())
print("\n Tipurile coloanelor :")
print(df.dtypes)


#Cerinta 2
df=nan_replace_df(df)

total_nan=df.isna().sum().sum()
print("\n Demonstratie - numar total de nan-uri ramase : ", total_nan);


#Cerinta 3

df_calitate_7=df[df['quality']>=7]
cale_fisier='data_out/vinuri_calitate_min7.csv'
df_calitate_7.to_csv(cale_fisier, index=False)

print(f"Fisierul a fost salvat cu succes la calea {cale_fisier}")

#Cerinta 4

top50_alcohol=df.sort_values(by='alcohol', ascending=False ).head(50)
top50_alcohol.to_csv('data_out/top50_alcool.csv', index=False)


#Cerinta 5

medii_pe_calitate = df.groupby('quality')[['alcohol', 'pH']].mean().reset_index()
medii_pe_calitate.to_csv('data_out/medii_pe_calitate.csv', index=False)


#Cerinta 6

df['aciditate_totala']=df['fixed acidity']+df['volatile acidity']+df['citric acid']

col_cerute=['quality', 'alcohol', 'aciditate_totala', 'pH']
df[col_cerute].to_csv('data_out/vinuri_cu_aciditate.csv', index=False)


#Cerinta 7

medii_alcool = df.groupby('quality')['alcohol'].mean()
calitate_max = medii_alcool.idxmax()
print("\nNota de calitate cu media alcohol maxima:", calitate_max)

df_calitate_max = pd.DataFrame({'quality': [calitate_max]})

cale_max_alcool = 'data_out/calitate_max_alcool.csv'
df_calitate_max.to_csv(cale_max_alcool, index=False)


#Cerinta 8

variabile_acp = ['fixed acidity', 'volatile acidity', 'citric acid', 'alcohol', 'quality']
matrice_corelatie = df[variabile_acp].corr()
matrice_corelatie.to_csv('data_out/R.csv')
print("\nMatricea de corelatie:")
print(matrice_corelatie)

#Cerinta 9

media_alc = df['alcohol'].mean()
std_alc = df['alcohol'].std()

df_std = pd.DataFrame()
df_std['alcohol'] = df['alcohol']
df_std['alcohol_std'] = (df['alcohol'] - media_alc) / std_alc
df_std.to_csv('data_out/alcohol_standardizat.csv', index=False)


#Cerinta 10
coloane_dist = ['fixed acidity', 'volatile acidity', 'alcohol']
x = df[coloane_dist]
x_std = (x - x.mean()) / x.std()
x_20 = x_std.head(20).values

d = cdist(x_20, x_20, metric='euclidean')

etichete = ['Vin_' + str(i + 1) for i in range(20)]
salvare_matrice(d, etichete, etichete, 'data_out/d_euclid_20.csv')

print("\nMatricea distantelor euclidiene (20x20) a fost salvata in data_out/d_euclid_20.csv")

