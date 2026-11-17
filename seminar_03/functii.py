import numpy as np
import pandas as pd


def medie_ponderata(tabel, coloane, coloana_pondere):
    valori = np.average(tabel[coloane], axis=0, weights=tabel[coloana_pondere])
    return pd.Series(valori, index=coloane)


def indici_localizare(tabel, coloane, coloana_populatie):
    # (angajati judet / angajati national) / (populatie judet / populatie nationala)
    pondere_activitate = tabel[coloane] / tabel[coloane].sum()
    pondere_populatie = tabel[coloana_populatie] / tabel[coloana_populatie].sum()
    return pondere_activitate.div(pondere_populatie, axis=0)
