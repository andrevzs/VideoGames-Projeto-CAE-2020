# Gráfico 3 (Barras) - Top 10 Gêneros mais vendidos
import pandas as pd
import matplotlib.pyplot as plt

# Ler CSV
vg = pd.read_csv('VideoGames.csv')

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

        # Se nao houver um intevalo de anos selecionado
        if ano_i == 0 and ano_f == 0:
            for j in range(len(lstgen)):
                # E se o genero da linha for igual ao genero atual checado
                if gnr == lstgen[j]:
                    total[j] += glob  # Somar o valor de vendas a lista do total,
                    # A posicao j representa o genero que esta sendo contabilizado

        else:  # Caso o usuario tenha definido um intervalo de anos
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
op = input('Deseja escolher um intervalo de anos? [S/N] ')
continuar = False
if op.upper() == 'N':
    ini = 0 
    fini = 0
if op.upper() == 'S':
    while not continuar:
        ini = int(input('\nDigite o primeiro ano: '))
        fini = int(input('Digite o segundo ano: '))
        if fini >= ini:
            continuar = True   
k = graf3(ini, fini)


plt.bar(k[0], k[1], color=['silver', 'salmon', 'bisque', 'gold', 'limegreen', 'turquoise', 'lightskyblue', 'plum', 'hotpink', 'crimson'])

plt.xlabel('Generos')
plt.ylabel('Vendas')
plt.title('Top 10 Generos Mais Vendidos')

plt.tight_layout()
plt.show()
