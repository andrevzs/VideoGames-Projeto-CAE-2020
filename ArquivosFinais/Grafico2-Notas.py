import pandas as pd

vg = pd.read_csv('../VideoGames.csv', sep=',')

# Usuário fornece gênero
print('= Opções de Gênero =\nAction, Sports, Misc, Role-Playing, Shooter,'
      '\nAdventure, Racing, Platform, Simulation, Fighting, Strategy, Puzzle')
gen = input('Escolha gênero: ')

# Listas com valores
n_critica   = []
n_jogadores = []

for i in range(len(vg)):
    li = vg.iloc[i]

    genero = li['Genre']
    cscore = li['Critic_Score']
    pscore = li['User_Score']

    # Se gênero = genero_fornecido:
    if gen == gen:
        if cscore == '':
            pass
        elif cscore == 'tbd':
            pass
        else:
            n_critica.append(cscore)  # Adiciona 'Critic Score' à lista critic
        if pscore == '':
            pass
        elif pscore == 'tbd':
        else:
            n_jogadores.append(pscore)  # Adiciona 'User Score' à lista player


print('Critic:', n_critica)
print('Player:', n_jogadores)

# Plot histograma barras agrupadas
