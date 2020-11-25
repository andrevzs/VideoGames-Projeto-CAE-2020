import pandas as pd

vg = pd.read_csv('VideoGames.csv', sep=',')  # vg = VideoGames.csv

# Todos os anos
anos        = []
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
            na_sales[j]    += nali
            eu_sales[j]    += euli
            jp_sales[j]    += jpli
            other_sales[j] += otli

na_arred = ['%.2f' % x for x in na_sales]
eu_arred = ['%.2f' % y for y in eu_sales]
jp_arred = ['%.2f' % z for z in jp_sales]
ot_arred = ['%.2f' % w for w in other_sales]

# Lista de vendas NA
# Soma(Ano1), Soma(Ano2), Soma(Ano3)...
print('NA Sales:', na_arred)
print('NA Total:', round(sum(na_sales)), 2)

print('\nEU Sales:', eu_arred)
print('EU Total', round(sum(eu_sales)), 2)

print('\nJP Sales:', jp_arred)
print('JP Total:', round(sum(jp_sales)), 2)

print('Other Sales:', ot_arred)
print('Other Total:', round(sum(other_sales)), 2)
