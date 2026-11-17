import os

import pandas as pd

from functii import medie_ponderata, indici_localizare

os.makedirs('data_out', exist_ok=True)

industria = pd.read_csv('data_in/IndustriaAlimentara.csv', index_col=0)
populatie = pd.read_csv('data_in/PopulatieLocalitati.csv', index_col=0)
coduri_judete = pd.read_csv('data_in/Coduri_Judete.csv', index_col=0)

activitati = list(industria.columns[1:])  # toate coloanele in afara de Localitate

# Cerinta 1
total_angajati = industria[activitati].sum(axis=1)
cerinta1 = industria[total_angajati > 0]
cerinta1.to_csv('data_out/Cerinta1.csv')

# Cerinta 2
# Procentele se calculeaza doar pentru localitatile cu angajati (evitam impartirea la 0)
cerinta2 = cerinta1[activitati].div(total_angajati[total_angajati > 0], axis=0) * 100
cerinta2.insert(0, 'Localitate', cerinta1['Localitate'])
cerinta2.round(2).to_csv('data_out/Cerinta2.csv')

# Cerinta 3
localitati = industria[activitati].join(populatie[['Judet', 'Populatie']], how='inner')
judete = localitati.groupby('Judet').sum()

cerinta3 = pd.DataFrame({
    'Pondere_procent': judete[activitati].sum(axis=1) / judete['Populatie'] * 100
}).sort_values('Pondere_procent', ascending=False)
cerinta3.round(4).to_csv('data_out/Cerinta3.csv')

# Cerinta 4
cerinta4 = pd.DataFrame({'Activitate': judete[activitati].idxmax(axis=1)})
cerinta4.to_csv('data_out/Cerinta4.csv')

# Cerinta 5
localitati = localitati.join(coduri_judete['Regiune'], on='Judet')
cerinta5 = localitati.groupby('Regiune')[activitati + ['Populatie']].apply(
    lambda grup: medie_ponderata(grup, activitati, 'Populatie')
)
cerinta5.round(3).to_csv('data_out/Cerinta5.csv')

# Cerinta 6
cerinta6 = indici_localizare(judete, activitati, 'Populatie')
cerinta6.round(3).to_csv('data_out/Cerinta6.csv')
print(cerinta6.round(3))