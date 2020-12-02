# Gráfico 4 - Total de Jogos /Plataforma
import pandas as pd
import matplotlib.pyplot as plt
vg = pd.read_csv('VideoGames.csv', sep=',')


def graf4():
    console = []
    njogos = []

    top_console = []
    top_njogos = []

    for i in range(len(vg)):
        li = vg.iloc[i]

        platf = li['Platform']

        if platf in console:
            pos = console.index(platf)
            njogos[pos] += 1
        else:
            console.append(platf)
            njogos.append(1)

    for j in range(0, 10):
        mxm = max(njogos)
        top_njogos.append(mxm)

        posj = njogos.index(mxm)
        top_console.append(console[posj])

        njogos[posj] = 0

    return top_console, top_njogos


x = graf4()

def plot(v):
    plt.style.use('dark_background')
    plt.rcParams['figure.facecolor'] = '#222831' 
    plt.rcParams['axes.facecolor'] = '#222831'
    plt.rcParams['text.color'] = '#ececec'
    plt.rcParams['xtick.color'] = '#ececec'
    plt.rcParams['ytick.color'] = '#ececec'
    plt.rcParams['axes.labelcolor'] = '#ececec'
    plt.title('Quantidade de jogos lancados para cada console')
    plt.xlabel('Consoles')
    plt.ylabel('Jogos')
    plt.bar(v[0], v[1])
    plt.show()

plot(x)
