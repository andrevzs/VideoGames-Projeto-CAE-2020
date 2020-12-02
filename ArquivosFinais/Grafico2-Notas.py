# VideoGames-Projeto-CAE-2020
# Grafico 2 - Notas para Genero

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>


# Funcao que gera e plota o grafico 2
def graf2():
    generos = ['ACTION', 'ADVENTURE', 'FIGHTING', 'MISC', 'PLATFORM', 'PUZZLE', 'RACING', 'ROLE-PLAYING', 'SHOOTER', 'SIMULATION', 'SPORTS', 'STRATEGY']

    rodar = True
    while rodar is True:
        valido1 = False
        valido2 = False

        # Usuário fornece gênero
        print('= Opcoes de Genero =\nAction, Sports, Misc, Role-Playing, Shooter,', '\nAdventure, Racing, Platform, Simulation, Fighting, Strategy, Puzzle')

        # Checagem de erros no input
        while valido1 is False:
            gen = input('\nDigite um genero: ')
            try:
                str(gen)
                if gen.upper() in generos:
                    valido1 = True
                else:
                    print('Oops... esse nao e um genero valido!')
                    valido1 = False
            except ValueError:
                print('Oops... esse nao e um genero valido!')

        while valido1 is True:
            # Listas com valores
            n_critica   = []
            n_players = []

            for i in range(len(vg)):
                li = vg.iloc[i]

                genero = str(li['Genre'])
                cscore = li['Critic_Score']
                pscore = li['User_Score']

                # Se gênero = genero_fornecido:
                if genero.upper() == gen.upper():
                    if not math.isnan(float(cscore)):
                        n_critica.append(cscore/10)  # Adiciona 'Critic Score' à lista critic
                    if not math.isnan(float(pscore)):
                        n_players.append(pscore)  # Adiciona 'User Score' à lista player

            # Plot histograma barras agrupadas
            # Eixo X: nota
            # Eixo Y: frequência
            plt.hist([n_players, n_critica], rwidth=0.85, color=['#30475e', '#f2a365'], label=['Players', 'Critica'])

            plt.xlabel('Nota Recebida', color='#ececec')
            plt.ylabel('Ocorrencias da Nota', color='#ececec')
            plt.title(f'Notas da Critica e dos Jogadores para o genero {gen.capitalize()}', fontweight='bold')

            plt.grid(True, which='both', axis='y', alpha=0.5, linestyle=':', color='#ececec')
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
            plt.tight_layout()
            plt.show()
            valido1 = False
            rodar   = False


graf2()
