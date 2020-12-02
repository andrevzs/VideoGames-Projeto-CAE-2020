# VideoGames-Projeto-CAE-2020
# Gráfico 3 (Barras) - Top 10 Gêneros mais vendidos

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>


# Gerar lista com total de vendas
total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Gerar lista de generos em ordem alfabética
lstgen = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle',
          'Racing', 'Role-Playing', 'Simulation', 'Shooter', 'Sports', 'Strategy']


# Funcao para somar valores de vendas
def graf3(ano_i, ano_f):
    # Execucao para todas linhas do CSV
    for i in range(len(vg)):
        li = vg.iloc[i]

        glob = float(li['Global_Sales'])   # Selecionar coluna de vendas 'Global Sales' (Soma de todas regioes)
        gnr  = li['Genre']                 # Selecionar coluna de genero
        ano  = int(li['Year_of_Release'])  # Selecionar coluna do ano de lançamento

        # Se o ano do CSV estiver entre os valores do intervalo
        if int(ano_i) <= ano <= int(ano_f):
            for j in range(len(lstgen)):
                if gnr == lstgen[j]:
                    total[j] += glob  # Somar o valor de vendas a lista do total

    # Lista com os 10 maiores valores de vendas e os 10 generos mais vendidos
    top10vendas = []
    top10gen = []

    for k in range(0, 10):
        maior = max(total)
        pos = total.index(maior)
        top10gen.append(lstgen[pos])
        top10vendas.append(maior)
        total.remove(maior)
        lstgen.remove(lstgen[pos])
        
    return top10gen, top10vendas
    

# Usuario deve informar os anos que deseja exibir
op_valida = False
while not op_valida:
    op = input('Deseja escolher um intervalo de anos? [S/N] ')
    try:
        str(op)
        if op.upper() == 'S' or op.upper() == 'N':
            op_valida = True
        else:
            print('Putz Grila! Voce causou um erro!\n'
                  'Digite apenas S ou N, por favor.\n')
            op_valida = False
    except ValueError:
        print('Putz Grila! Voce causou um erro!\n'
              'Digite apenas S ou N, por favor.\n')
        op_valida = False

ano1_valido = False
ano2_valido = False

if op_valida:
    if op.upper() == 'N':
        ano1 = 1977
        ano2 = 2018
        ano1_valido = True
        ano2_valido = True
    if op.upper() == 'S':
        while not ano1_valido:
            ano1 = input('Digite o primeiro ano: ')
            try:
                int(ano1)
                if 1977 <= int(ano1) <= 2018:
                    ano1_valido = True
                else:
                    print('- ERRO! -\nDigite um ano entre 1977 e 2018.\n')
                    ano1_valido = False
            except ValueError:
                print('Errou! Digite o ano como um numero inteiro de 4 digitos!\n')
                ano1_valido = False

        if ano1_valido:
            while not ano2_valido:
                ano2 = input('Digite o segundo ano: ')
                try:
                    int(ano2)
                    if int(ano1) <= int(ano2) <= 2018:
                        ano2_valido = True
                    else:
                        print(f'- ERRO! -\nDigite um ano entre {ano1} e 2018.\n')
                        ano2_valido = False
                except ValueError:
                    print('Errou! Digite o ano como um numero inteiro de 4 digitos!\n')
                    ano2_valido = False

if ano2_valido:
    a = graf3(ano1, ano2)
    # Usuario deve informar quais cores deseja no grafico
    lst_cores = {'PRATA': 'silver', 'SALMAO': 'salmon', 'CREME': 'bisque', 'DOURADO': 'gold',
                 'VERDE-LIMAO': 'limegreen',
                 'TURQUESA': 'turquoise', 'AZUL': 'lightskyblue', 'ROSINHA': 'plum', 'ROSA': 'hotpink',
                 'VERMELHO': 'crimson'}
    cores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    escolhido = []
    lista = ['Prata', 'Salmao', 'Creme', 'Dourado', 'Verde-Limao', 'Turquesa', 'Azul', 'Rosinha', 'Rosa', 'Vermelho']
    for b in range(0, 10):
        print(f'Digite um numero para selecionar uma cor para {a[0][b]}:\n')
        for i in range(len(lista)):
            print(f"        [{i}]   {lista[i]}")
        print()
        cores[b] = int(input("Escolha uma cor: "))
        escolhido.append(lista[cores[b]].upper())
        lista.remove(lista[cores[b]])


plt.bar(a[0], a[1], color=[lst_cores[escolhido[0]], lst_cores[escolhido[1]], lst_cores[escolhido[2]],
                           lst_cores[escolhido[3]], lst_cores[escolhido[4]], lst_cores[escolhido[5]],
                           lst_cores[escolhido[6]], lst_cores[escolhido[7]], lst_cores[escolhido[8]],
                           lst_cores[escolhido[9]]])

plt.xlabel('Generos')
plt.ylabel('Vendas')
plt.title('Top 10 Generos Mais Vendidos', fontweight='bold')

plt.grid(True, which='both', axis='y', alpha=0.5, linestyle=':', color='#ececec')
plt.tight_layout()
plt.show()
