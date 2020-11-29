# Gráfico 5 - Vendas / Publisher escolhida
import pandas as pd
import matplotlib.pyplot as plt

vg = pd.read_csv('VideoGames.csv', sep=',')

anos = []
na = []
eu = []
jp = []
ot = []

print('Exemplos de publishers:\n'
      'Nintendo, Microsoft, Take-Two, Sony, Activision,\n'
      'Ubisoft, Bethesda, Electronic Arts, Capcom, Sega\n')
publisher = input('Digite uma publisher: ')

for i in range(len(vg)):
    li    = vg.iloc[i]

    pub   = str(li['Publisher'])
    nali = float(li['NA_Sales'])
    euli = float(li['EU_Sales'])
    jpli = float(li['JP_Sales'])
    otli = float(li['Other_Sales'])
    ano   = int(li['Year_of_Release'])

    if str(publisher).upper() in pub.upper():
        if ano in anos:
            pass
        else:
            anos.append(ano)
            na.append(0)
            eu.append(0)
            jp.append(0)
            ot.append(0)


anos = list(set(anos))

for j in range(len(vg)):
    li = vg.iloc[j]

    pub = str(li['Publisher'])
    nali = float(li['NA_Sales'])
    euli = float(li['EU_Sales'])
    jpli = float(li['JP_Sales'])
    otli = float(li['Other_Sales'])
    ano = int(li['Year_of_Release'])

    for k in range(len(anos)):
        if ano == anos[k]:
            if str(publisher).upper() in pub.upper():
                na[k] += nali
                eu[k] += euli
                jp[k] += jpli
                ot[k] += otli

plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#222831'
plt.rcParams['axes.facecolor'] = '#222831'
plt.rcParams['text.color'] = '#ececec'
plt.rcParams['xtick.color'] = '#ececec'
plt.rcParams['ytick.color'] = '#ececec'
plt.rcParams['axes.labelcolor'] = '#ececec'


plt.plot(anos, na, label='Vendas NA')
plt.plot(anos, eu, label='Vendas EU')
plt.plot(anos, jp, label='Vendas JP')
plt.plot(anos, ot, label='Outras Regiões')

plt.xlabel('Anos', color='#ececec')
plt.ylabel('Nº de vendas em milhões', color='#ececec')
plt.title(f'Número de Vendas da {publisher.title()}', fontweight='bold')

plt.grid(True, which='both', axis='both', alpha=0.5, linestyle=':', color='#ececec')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
plt.tight_layout()
plt.show()
