# VideoGames-Projeto-CAE-2020
# Gráfico 6 - Média de Notas p/ ano

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>
from pandas import *
import matplotlib.pyplot as plt
import math
abrir = read_csv('VideoGames.csv', sep=",")


# Funcao que ira calcular os dados para o grafico
def graf6(x, y):
    # Lista com anos possiveis
    anos = [1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
            1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
            2004, 2005, 2006, 2007, 2008, 2009, 2010,
            2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

    # Listas de notas que serao somadas para cada ano
    nota_critica = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nota_usuario = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    qnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Execucao para todas as linhas do CSV
    for i in range(len(abrir)):
        linha = abrir.iloc[i]

        critica = linha['Critic_Score']
        usuario = linha['User_Score']
        ano = linha['Year_of_Release']

        # Se o ano i estiver entre ou for igual ao ano1 e ano2
        # E nao for texto (!= NaN)
        # Adicionar o valor na lista
        if x <= int(ano) <= y:
            pos = anos.index(ano)
            if not math.isnan(float(critica)):
                nota_critica[pos] += critica/10
                qnt[pos] += 1
            if not math.isnan(float(usuario)):
                nota_usuario[pos] += usuario
        if x == 0:
            pos = anos.index(ano)
            if not math.isnan(float(critica)):
                nota_critica[pos] += critica/10
                qnt[pos] += 1
            if not math.isnan(float(usuario)):
                nota_usuario[pos] += usuario

    media_usuario = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    media_critica = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Calculo do numero de notas pra fazer a media
    for j in range(len(anos)):
        if qnt[j] != 0:

            a = int(nota_critica[j])/int(qnt[j])
            b = int(nota_usuario[j])/int(qnt[j])
            media_critica[j] = a
            media_usuario[j] = b
    return anos, media_critica, media_usuario, qnt


# Input do usuario
op_valida = False
while not op_valida:
    op = input('Deseja escolher um intervalo de anos? [S/N] ')
    # Checagem de erros
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

ano1_valido = False
ano2_valido = False

# O codigo so continua se a opcao escolhida for valida
if op_valida:
    continuar = False
    if op.upper() == 'N':
        ano1 = 0
        ano2 = 0
        ano1_valido = True
        ano2_valido = True

    if op.upper() == 'S':
        while not continuar:
            while not ano1_valido:
                ano1 = input('Digite o primeiro ano: ')
                try:
                    int(ano1)
                    if 1977 <= int(ano1) <= 2018:
                        ano1_valido = True
                    else:
                        print('Ah nao! Deu erro!\n'
                              'Por favor escolha um ano apenas entre 1977 e 2018.\n')
                        ano1_valido = False
                except ValueError:
                    print('- ERRO -\nDigite o ano como um numero inteiro de 4 digitos\n')
                    ano1_valido = False
            if ano1_valido:
                while not ano2_valido:
                    ano2 = input('Digite o segundo ano: ')
                    try:
                        int(ano2)
                        if int(ano1) <= int(ano2) <= 2018:
                            ano2_valido = True
                            continuar = True
                        else:
                            print('Ah nao! Deu erro!\n'
                                    f'Por favor escolha um ano apenas entre {ano1} e 2018.\n')
                            ano2_valido = False
                    except ValueError:
                        print('Digite o ano como um numero inteiro de 4 digitos\n')
                        ano2_valido = False


# Funcao de plotagem do grafico
def plot6(ano, mediaC, mediaU):
    plt.plot(ano, mediaC, label='Media Criticos')
    plt.plot(ano, mediaU, label='Media Usuarios')

    if ano1 == 0 and ano2 == 0:
        plt.axis([1977, 2020, 0, 10])
    else:
        plt.axis([ano1, ano2, 0, 10])

    plt.xlabel('Anos', color='#ececec')
    plt.ylabel('Notas', color='#ececec')
    plt.title('Media de notas por ano Critico x Usuarios', fontweight='bold')

    plt.grid(True, which='both', axis='both', alpha=0.5, linestyle=':', color='#ececec')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
    plt.tight_layout()
    plt.show()


# Se o input do usuario for valido, plotar o grafico
if ano2_valido:
    ano1 = int(ano1)
    ano2 = int(ano2)
    a = graf6(ano1, ano2)

    plot6(a[0], a[1], a[2])
