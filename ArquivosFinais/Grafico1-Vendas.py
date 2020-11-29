import pandas as pd
import matplotlib.pyplot as plt

vg = pd.read_csv('VideoGames.csv', sep=',')

def grafico1(x, y): # x = ano de inicio do intervalo de tempo; y = ano de fim do intervalo de tempo.
    anos = []
    periodo = []
    na_sales    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    eu_sales    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    jp_sales    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    other_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(vg)):
        li = vg.iloc[i]

        anoli = int(li['Year_of_Release'])
        anos.append(anoli)

    anos = list(set(anos))
    for i in range(len(vg)):
        li = vg.iloc[i]

        anoli = int(li['Year_of_Release'])
        nali  = float(li['NA_Sales'])
        euli  = float(li['EU_Sales'])
        jpli  = float(li['JP_Sales'])
        otli  = float(li['Other_Sales'])
        for j in range(len(anos)):
            if anoli == anos[j]:
                    if x == 0 and y == 0:
                        na_sales[j]    += nali
                        eu_sales[j]    += euli
                        jp_sales[j]    += jpli
                        other_sales[j] += otli
                    if x <= anoli <= y:
                        na_sales[j]    += nali
                        eu_sales[j]    += euli
                        jp_sales[j]   += jpli
                        other_sales[j] += otli

    return anos, na_sales, eu_sales, jp_sales, other_sales

op = input('Deseja escolher um intervalo de anos? [S/N] ')
if op.upper() == 'N':
    ini = 0 
    fini = 0
if op.upper() == 'S':
    ini = int(input('\nDigite o primeiro ano: '))
    fini = int(input('Digite o segundo ano: '))

k = grafico1(ini, fini)

def plot1(ano, na, eu, jp, other):

    plt.plot(ano, na, label='Vendas NA')
    plt.plot(ano, eu, label='Vendas EU')
    plt.plot(ano, jp, label='Vendas JP')
    plt.plot(ano, other, label='Outras Regioes')

    if fini == 0:
        plt.axis([1977, 2019, 0, 400])
    else:
        plt.axis([ini, fini, 0, max(na) + 25])
    plt.ylabel('Nº de vendas em milhoes')
    plt.xlabel('Anos')
    plt.title('Numero de Vendas - Regiao/Ano')
    plt.legend()
    plt.show()


plot1(k[0], k[1], k[2], k[3], k[4])
