import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

from functii import standardizare, corelograma, nr_componente_prag, plot_varianta

os.makedirs('data_out', exist_ok=True)

# Cerinta 1 - incarcarea datelor si selectarea celor 6 variabile de cheltuieli
tabel = pd.read_csv('data_in/Wholesale customers data.csv')
variabile = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']
x = tabel[variabile]

print('Dimensiune set de date:', tabel.shape)
print(x.describe().round(2))

# Cerinta 2 - standardizarea variabilelor
x_std = standardizare(x)
x_std.round(4).to_csv('data_out/x_std.csv')

# Cerinta 3 - matricea de corelatie si corelograma cu seaborn
r = x.corr()
r.round(3).to_csv('data_out/R.csv')
corelograma(r, 'Matricea de corelatie - Wholesale customers', 'data_out/corelograma.png')

# Cerinta 4 - ACP si varianta explicata de fiecare componenta
acp = PCA()
c = acp.fit_transform(x_std)

etichete_comp = ['C' + str(i + 1) for i in range(len(variabile))]
pd.DataFrame(c, index=x.index, columns=etichete_comp).round(4).to_csv('data_out/componente.csv')

tabel_varianta = pd.DataFrame({
    'Valori proprii': acp.explained_variance_,
    'Varianta explicata': acp.explained_variance_ratio_,
    'Varianta cumulata': np.cumsum(acp.explained_variance_ratio_)
}, index=etichete_comp)
tabel_varianta.round(4).to_csv('data_out/varianta.csv')
print('\nVarianta explicata de componente:')
print(tabel_varianta.round(4))

# Cerinta 5 - numarul de componente care explica cel putin 80% din varianta
prag = 0.8
k = nr_componente_prag(tabel_varianta['Varianta cumulata'].values, prag)
print(f'\nSunt necesare {k} componente pentru a explica cel putin {prag:.0%} din varianta totala '
      f'({tabel_varianta["Varianta cumulata"].iloc[k - 1]:.2%}).')
plot_varianta(tabel_varianta, prag, 'data_out/varianta.png')

plt.show()