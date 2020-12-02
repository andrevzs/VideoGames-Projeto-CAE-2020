# Gráfico 4 - Total de Jogos /Plataforma

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>


# Funcao que calcula os valores usados pro grafico 4
def graf4():
    # Lista de consoles e lista de respectivos valores de jogos vendidos
    console = []
    njogos = []

    # Lista dos 10 consoles mais vendidos e seus respectivos valores
    top_console = []
    top_njogos = []

    # Execucao para todas as linhas do CSV
    for i in range(len(vg)):
        li = vg.iloc[i]

        platf = li['Platform']  # Selecionar coluna que fornece a plataforma do jogo

        # Se a plataforma da linha atual ja estiver na lista de consoles, somar 1 na lista de jogos desse console
        if platf in console:
            pos = console.index(platf)
            njogos[pos] += 1
        # Se a plataforma nao estiver na lista de consoles, adiciona-la a lista de consoles e somar 1 na lista de jogos
        else:
            console.append(platf)
            njogos.append(1)

    # Selecao dos 10 mais vendidos
    for j in range(0, 10):
        mxm = max(njogos)
        top_njogos.append(mxm)

        posj = njogos.index(mxm)
        top_console.append(console[posj])

        njogos[posj] = 0

    return top_console, top_njogos


# Funcao que gera o grafico
def plot(v):
    plt.xlabel('Consoles')
    plt.ylabel('Jogos')
    plt.title('Quantidade de Jogos Lancados para Cada Console', fontweight='bold')

    plt.bar(v[0], v[1], color=['silver', 'salmon', 'bisque', 'gold', 'limegreen', 'turquoise', 'lightskyblue', 'plum', 'hotpink', 'crimson'])

    plt.grid(True, which='both', axis='y', alpha=0.5, linestyle=':', color='#ececec')
    plt.tight_layout()
    plt.show()


# Chamada da funcao que ira plotar o grafico
plot(graf4())
