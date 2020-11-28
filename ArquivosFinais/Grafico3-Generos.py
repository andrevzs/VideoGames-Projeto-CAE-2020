# Gráfico 3 (Barras) - Top 10 Gêneros mais vendidos
import pandas as pd

# ler CSV
vg = pd.read_csv('../VideoGames.csv')

# Gerar lista com total de vendas
total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Gerar lista de gêneros em ordem alfabética
lstgen = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle',
          'Racing', 'Role-Playing', 'Simulation', 'Shooter', 'Sports', 'Strategy']


# Função para somar valores de vendas
def graf3(ano_i, ano_f):
    # Execução para todas linhas do CSV
    for i in range(len(vg)):
        li = vg.iloc[i]

        glob = float(li['Global_Sales'])  # Selecionar coluna de vendas 'Global Sales' (Soma de todas regiões)
        gnr = li['Genre']                 # Selecionar coluna de Gênero
        ano = int(li['Year_of_Release'])  # Selecionar coluna do ano de lançamento

        # Apenas se não houver um intevalo de anos selecionado
        if ano_i == 0 and ano_f == 0:
            # Se o genero da linha for igual ao genero atual checado, somar na posição i
            for j in range(len(lstgen)):
                if gnr == lstgen[j]:
                    total[j] += glob
        # Caso o usuário tenha definido um intervalo de anos
        else:
            if int(ano_i) <= ano <= int(ano_f):
                for j in range(len(lstgen)):
                    if gnr == lstgen[j]:
                        total[j] += glob

    return total


op = input('Deseja escolher um intervalo de anos? [S/N] ')
if op.upper() == 'N':
    graf3(0, 0)
if op.upper() == 'S':
    ini = int(input('\nDigite o primeiro ano: '))
    fin = int(input('Digite o segundo ano: '))
    graf3(ini, fin)

# Calcular 10 maiores valores
top10 = []

for a in range(0, 5):
    max1 = 0

    for b in range(len(total)):
        if int(total[b]) > max1:
            max1 = total[b]

        total.remove(max1)
        top10.append(max1)


print(total)
print(top10)
