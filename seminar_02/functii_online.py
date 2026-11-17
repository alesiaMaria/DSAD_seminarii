import pandas as pd

#Cerinta 2 :
def nan_replace_df(tabel):
    tabel_numeric=tabel.select_dtypes(include='number')
    tabel[tabel_numeric.columns]=tabel_numeric.fillna(tabel_numeric.mean())
    return tabel

#Cerinta Bonus :
def salvare_matrice(x, index_linie, index_coloana, fisier):
    tabel = pd.DataFrame(x, index=index_linie, columns=index_coloana)
    tabel.to_csv(fisier)
    return tabel
















