import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb


def standardizare(tabel):
    # Deviatia standard de populatie (ddof=0), la fel ca StandardScaler din sklearn
    return (tabel - tabel.mean()) / tabel.std(ddof=0)


def corelograma(r, titlu, fisier):
    plt.figure(figsize=(9, 7))
    plt.title(titlu)
    sb.heatmap(r, vmin=-1, vmax=1, cmap='RdYlBu', annot=True, fmt='.2f')
    plt.tight_layout()
    plt.savefig(fisier)


def nr_componente_prag(varianta_cumulata, prag=0.8):
    # Prima componenta la care varianta cumulata atinge pragul
    return int(np.argmax(varianta_cumulata >= prag)) + 1


def plot_varianta(tabel_varianta, prag, fisier):
    k = range(1, len(tabel_varianta) + 1)
    plt.figure(figsize=(8, 5))
    plt.title('Varianta explicata de componentele principale')
    plt.bar(k, tabel_varianta['Varianta explicata'], label='Varianta explicata')
    plt.plot(k, tabel_varianta['Varianta cumulata'], 'ro-', label='Varianta cumulata')
    plt.axhline(prag, color='g', linestyle='--', label=f'Prag {prag:.0%}')
    plt.xticks(k, tabel_varianta.index)
    plt.ylabel('Procent din varianta totala')
    plt.legend()
    plt.tight_layout()
    plt.savefig(fisier)