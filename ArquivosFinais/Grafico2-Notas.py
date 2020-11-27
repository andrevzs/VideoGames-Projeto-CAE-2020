import pandas as pd
import math
import matplotlib.pyplot as plt

vg = pd.read_csv('../VideoGames.csv', sep=',')

# Usuário fornece gênero
print('= Opções de Gênero =\nAction, Sports, Misc, Role-Playing, Shooter,', '\nAdventure, Racing, Platform, Simulation, Fighting, Strategy, Puzzle')
gen = input('Digite um gênero: ')

# Listas com valores
n_critica   = []
n_players = []

for i in range(len(vg)):
    li = vg.iloc[i]

    genero = li['Genre']
    cscore = li['Critic_Score']
    pscore = li['User_Score']

    # Se gênero = genero_fornecido:
    if genero == gen:
        if not math.isnan(float(cscore)):
            n_critica.append(cscore/10)  # Adiciona 'Critic Score' à lista critic
        if not math.isnan(float(pscore)):
            n_players.append(pscore)  # Adiciona 'User Score' à lista player


# print('Critic:', n_critica)
# print('Player:', n_players)

# Plot histograma barras agrupadas
# Eixo X: nota
# Eixo Y: frequência

np, binsp, patchesp = plt.hist(n_players, bins='auto', rwidth=0.85)
nc, binsc, patchesc = plt.hist(n_critica, bins='auto', rwidth=0.85)

plt.xlabel('Valor')
plt.ylabel('Ocorrências')
plt.title('Notas')

plt.show()
