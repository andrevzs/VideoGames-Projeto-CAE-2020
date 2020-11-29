# Gráfico 4 - Total de Jogos /Plataforma
import pandas as pd

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

    for j in range(len(console)):
        mxm = max(njogos)
        top_njogos.append(mxm)

        posj = njogos.index(mxm)
        top_console.append(console[posj])

        njogos[posj] = 0

    return top_console, top_njogos


x = graf4()

for a in range(len(x[0])):
    print(f'O console {x[0][a]} recebeu {x[1][a]} jogos.')
