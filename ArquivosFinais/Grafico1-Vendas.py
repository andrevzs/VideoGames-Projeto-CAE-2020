# VideoGames-Projeto-CAE-2020
# Grafico 1 - Vendas de Regiao por Ano

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>
import matplotlib.pyplot as plt
import pandas as pd
vg = pd.read_csv('VideoGames.csv', sep=",")

def graf1(x, y):  # x = ano inicial do intervalo de tempo, y = ano final do intervalo de tempo
    anos = []  # Lista de anos

    # Listas de vendas para cada regiao
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
        li = vg.iloc[i]  # Definicao de como ler as linhas do CSV

        anoli = int(li['Year_of_Release'])  # Definicao dos valores de ano
        anos.append(anoli)  # Os valores de ano sao apendados na lista de anos

    # Remocao de anos duplicados da lista
    # Com a funcao set ela tambem ja fica ordenada do menor ao maior
    anos = list(set(anos))

    # Agora sao preenchidas as listas de vendas em ordem de anos
    for i in range(len(vg)):
        li = vg.iloc[i]

        anoli = int(li['Year_of_Release'])
        nali  = float(li['NA_Sales'])
        euli  = float(li['EU_Sales'])
        jpli  = float(li['JP_Sales'])
        otli  = float(li['Other_Sales'])

        for j in range(len(anos)):
            # Se o ano da linha [j] do CSV for igual ao ano [j] da lista de anos
            # O valor de vendas de cada regiao é adicionado a sua respectiva lista
            if anoli == anos[j]:
                # Executa se nao forem especificados anos pelo usuario
                if x == 0 and y == 0:
                    na_sales[j]    += nali
                    eu_sales[j]    += euli
                    jp_sales[j]    += jpli
                    other_sales[j] += otli
                # Executa para o intervalo informado pelo usuario
                elif int(x) <= anoli <= int(y):
                    na_sales[j]    += nali
                    eu_sales[j]    += euli
                    jp_sales[j]    += jpli
                    other_sales[j] += otli

    # A funcao retorna as listas que serao usadas para plotar o grafico
    return anos, na_sales, eu_sales, jp_sales, other_sales


def mostrar(ano, na, eu, jp, other):
    plt.plot(ano, na,    label='Vendas NA',      linewidth=2.5)
    plt.plot(ano, eu,    label='Vendas EU',      linewidth=2.5)
    plt.plot(ano, jp,    label='Vendas JP',      linewidth=2.5)
    plt.plot(ano, other, label='Outras Regioes', linewidth=2.5)

    if ano2 == 0:
        plt.axis([1977, 2019, 0, 400])
    else:
        plt.axis([int(ano1), int(ano2), 0, max(na) + 25])

    plt.xlabel('Anos')
    plt.ylabel('Numero de vendas em milhoes')
    plt.title('Numero de Vendas Regioes/Ano', fontweight='bold')

    plt.grid(True, which='both', axis='both', alpha=0.5, linestyle=':', color='#ececec')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
    plt.tight_layout()
    plt.show()


# Input do usuario
op_valida = False
while not op_valida:
    op = input('Deseja escolher um intervalo de anos? [S/N] ')
    # Checagem de erros do usuario
    try:
        str(op)
        if op.upper() == 'S' or op.upper() == 'N':
            op_valida = True
        else:
            print('Opa! Algo deu errado, digite apenas S ou N.\n')
            op_valida = False
    except ValueError:
        print('Opa! Algo deu errado, digite apenas S ou N.\n')
        op_valida = False

# O codigo so continua executando se a opcao escolhida pelo usuario for valida
if op_valida:
    continuar = False
    if op.upper() == 'N':
        ano1 = 0
        ano2 = 0
    if op.upper() == 'S':
        while not continuar:
            ano1_valido = False
            ano2_valido = False
            while not ano1_valido:
                ano1 = input('Digite o primeiro ano: ')
                try:
                    int(ano1)
                    if 1977 <= int(ano1) <= 2018:
                        ano1_valido = True
                    else:
                        print('Caramba, deu erro!\n'
                              'Por favor escolha um ano apenas entre 1977 e 2018.\n')
                        ano1_valido = False
                except ValueError:
                    print('Digite o ano como um numero inteiro de 4 digitos!\n')
                    ano1_valido = False
            if ano1_valido:
                while not ano2_valido:
                    ano2 = input('Digite o segundo ano: ')
                    try:
                        int(ano2)
                        if int(ano2) >= int(ano1):
                            ano2_valido = True
                            continuar = True
                        else:
                            print('Caramba, deu erro!\n'
                                  f'Por favor escolha um ano apenas entre {ano1} e 2018.\n')
                            ano2_valido = False
                    except ValueError:
                        print('Digite o ano como um numero inteiro de 4 digitos!\n')
                if ano2_valido:
                    # Variavel que quando chamada executa a funcao de calculo dos dados que irao para o grafico
                    exe = graf1(ano1, ano2)

mostrar(exe[0], exe[1], exe[2], exe[3], exe[4])
