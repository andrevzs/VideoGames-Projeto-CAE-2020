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


def graf6(x, y):
    anos = [1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
            1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
            2004, 2005, 2006, 2007, 2008, 2009, 2010,
            2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    nota_critico = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nota_usuario = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    qnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(abrir)):
        linha = abrir.iloc[i]
        critico = linha['Critic_Score']
        usuario = linha['User_Score']
        ano = linha['Year_of_Release']
        if x <= ano <= y:
            pos = anos.index(ano)
            if not math.isnan(float(critico)):
                nota_critico[pos] += critico/10
                qnt[pos] += 1
            if not math.isnan(float(usuario)):
                nota_usuario[pos] += usuario
        if x == 0:
            pos = anos.index(ano)
            if not math.isnan(float(critico)):
                nota_critico[pos] += critico/10
                qnt[pos] += 1
            if not math.isnan(float(usuario)):
                nota_usuario[pos] += usuario
    media_usuario = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    media_critica = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(len(anos)):
        if qnt[j] != 0:

            a = int(nota_critico[j])/int(qnt[j])
            b = int(nota_usuario[j])/int(qnt[j])
            media_critica[j] = a
            media_usuario[j] = b
    return anos, media_critica, media_usuario, qnt


op = input('Deseja escolher um intervalo de anos? [S/N] ')
continuar = False
if op.upper() == 'N':
    ini = 0
    fini = 0
if op.upper() == 'S':
    while continuar == False:
        ini = int(input('\nDigite o primeiro ano: '))
        fini = int(input('Digite o segundo ano: '))
        if fini >= ini:
            continuar = True


def plot6(ano, mediaC, mediaU):
    plt.plot(ano, mediaC, label='Media Criticos')
    plt.plot(ano, mediaU, label='Media Usuarios')

    if ini == 0 and fini == 0:
        plt.axis([1977, 2020, 0, 10])
    else:
        plt.axis([ini, fini, 0, 10])

    plt.xlabel('Anos', color='#ececec')
    plt.ylabel('Notas', color='#ececec')
    plt.title('Media de notas por ano Critico x Usuarios', fontweight='bold')

    plt.grid(True, which='both', axis='both', alpha=0.5, linestyle=':', color='#ececec')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
    plt.tight_layout()
    plt.show()


x = graf6(ini, fini)

plot6(x[0], x[1], x[2])
