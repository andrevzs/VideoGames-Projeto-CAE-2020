import pandas as pd
import math
import matplotlib.pyplot as plt

vg = pd.read_csv('VideoGames.csv', sep=',')

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
cores = ['b', 'g']
fig, ax1 = plt.subplots()
plt.title('Notas')
ax1.hist([n_players,n_critica],color=cores)
plt.tight_layout()
plt.xlabel('Valor')
plt.ylabel('Ocorrências')
plt.show()
