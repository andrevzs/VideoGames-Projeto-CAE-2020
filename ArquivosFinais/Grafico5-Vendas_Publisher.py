# VideoGames-Projeto-CAE-2020
# Gráfico 5 - Vendas / Publisher escolhida

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>

# Listas que serao usadas para calcular os dados
anos = []
na   = []
eu   = []
jp   = []
ot   = []

print('Exemplos de publishers:\n'
      'Nintendo, Microsoft, Take-Two, Sony, Activision,\n'
      'Ubisoft, Bethesda, Electronic Arts, Capcom, Sega\n')
# Input do usuario para procurar uma publisher
publisher = input('Digite uma publisher: ')

# Execucao para todas as linhas do CSV
for i in range(len(vg)):
    li    = vg.iloc[i]

    # Definicao de cada coluna necessaria
    pub   = str(li['Publisher'])
    nali  = float(li['NA_Sales'])
    euli  = float(li['EU_Sales'])
    jpli  = float(li['JP_Sales'])
    otli  = float(li['Other_Sales'])
    ano   = int(li['Year_of_Release'])

    # Se o que foi digitado pelo usuario estiver contido dentro de alguma publisher do CSV
    if str(publisher).upper() in pub.upper():
        # Se o ano atual estiver na coluna de anos
        if ano in anos:
            pass  # Ignorar
        # Caso contrario
        else:
            # Somar o ano na lista e adicionar uma casa vazia para as listas de vendas
            anos.append(ano)
            na.append(0)
            eu.append(0)
            jp.append(0)
            ot.append(0)


# Lista de anos ordenada em ordem crescente e anos duplicados sao removidos
anos = list(set(anos))


# Execucao para todas as linhas do CSV
for j in range(len(vg)):
    li = vg.iloc[j]

    # Definicao de cada coluna necessaria
    pub = str(li['Publisher'])
    nali = float(li['NA_Sales'])
    euli = float(li['EU_Sales'])
    jpli = float(li['JP_Sales'])
    otli = float(li['Other_Sales'])
    ano = int(li['Year_of_Release'])

    for k in range(len(anos)):
        # Caso o ano k da lista de anos corresponda ao ano k do CSV
        # Valores de vendas sao somados
        if ano == anos[k]:
            if str(publisher).upper() in pub.upper():
                na[k] += nali
                eu[k] += euli
                jp[k] += jpli
                ot[k] += otli


# Plotagem do grafico
plt.plot(anos, na, label='Vendas NA')
plt.plot(anos, eu, label='Vendas EU')
plt.plot(anos, jp, label='Vendas JP')
plt.plot(anos, ot, label='Outras Regiões')

plt.xlabel('Anos', color='#ececec')
plt.ylabel('Num de vendas em milhões', color='#ececec')
plt.title(f'Numero de Vendas da {publisher.title()}', fontweight='bold')

plt.grid(True, which='both', axis='both', alpha=0.5, linestyle=':', color='#ececec')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
plt.tight_layout()
plt.show()
