# VideoGames-Projeto-CAE-2020
# Menu

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>

# Importacao de bibliotecas que serao usadas no programa
import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'  # Funcao que impede o pygame de exibir a mensagem de boas vindas
import pygame
import random


# Configuracoes para a plotagem dos graficos
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#222831'  # Cor da parte externa do grafico
plt.rcParams['axes.facecolor']   = '#222831'  # Cor da parte interna do grafico
plt.rcParams['text.color']       = '#ececec'  # Cor de textos
plt.rcParams['xtick.color']      = '#ececec'  # Cor do eixo x
plt.rcParams['ytick.color']      = '#ececec'  # Cor do eixo y
plt.rcParams['axes.labelcolor']  = '#ececec'  # Cor dos rotulos dos eixos


# Codigo principal
# Leitura do arquivo CSV
vg = pd.read_csv('VideoGames.csv', sep=',')

# Variavel que faz o menu continuar sendo exibido
exibir = True

print('')  # Linha vazia apenas para estetica
print('='*14, 'VIDEOGAMES - Projeto CAE 2020', '='*15)  # Titulo do menu

# Enquanto o menu nao for encerrado pelo usuario:
while exibir:
    # Mostrar informacoes do programa
    print('=-'*30, '\n'
                   ' Esse programa consegue exibir graficos fazendo uso de um\n'
                   ' arquivo CSV que contem diversos dados estatisticos sobre\n'
                   ' videogames entre os anos de 1977 e 2018.\n\n'
                   ' Se quiser, digite uma das opcoes para exibir um grafico:')
    # Mostrar opcoes de grafico
    print('=-'*30, '\n'
          '[1] Vendas de Jogos por Regiao                (Graf. Linhas)\n'
          '[2] Frequencia de Notas (Review)              (Graf. Barras)\n'
          '[3] 10 Generos Mais Vendidos                  (Graf. Barras)\n'
          '[4] Num. de Jogos por Plataforma              (Graf. Barras)\n'
          '[5] Vendas por Publisher                      (Graf. Linhas)\n'
          '[6] Media de Notas por Ano                    (Graf. Linhas)\n'
          '[0] Encerrar programa')
    print('~'*60)

    op_valida = False  # Boolenao dependente da opcao digitada pelo usuario ser valida ou nao
    # Enquanto a opcao nao for valida, pedir opcao para o usuario, e checar validade
    while not op_valida:
        opcao = input('Opcao: ')
        try:
            # Se for possivel converter o input do usuario para um numero inteiro, retorna True, caso contrario, retorna False
            int(opcao)
            if int(opcao) == 100:  # Opcao secreta
                exec(open('snek.py').read())
            if 0 <= int(opcao) <= 6:  # Se a opcao estiver no menu (de 0 a 6), a opcao se torna valida
                op_valida = True
            # Caso o usuario nao escolha a opcao secreta e digite uma opcao que nao esta no menu
            else:
                print('Putz! Só tem 5 opções no menu!\n')  # Essa mensagem de erro é exibida e o input é solicitado novamente
                op_valida = False
        # Caso aconteca um erro por nao ser possivel converter o input para um numero inteiro
        # O input é solicitado novamente
        except ValueError:
            print('= Oops... você deve digitar a opção como um número inteiro! =\n')
            op_valida = False

    # Caso a opcao digitada pelo usuario seja valida
    # Ocorre a execucao dos programas para cada grafico
    # Cada grafico foi escrito em um arquivo .py separado que é aberto usando a funcao exec(open('...').read())
    if op_valida:
        # Gráfico 1
        if int(opcao) == 1:
            exec(open('Grafico1-Vendas.py').read())

        # Gráfico 2
        elif int(opcao) == 2:
            exec(open('Grafico2-Notas.py').read())

        # Gráfico 3
        elif int(opcao) == 3:
            exec(open('Grafico3-Generos.py').read())

        # Gráfico 4
        elif int(opcao) == 4:
            exec(open('Grafico4-Jogos.py').read())

        # Gráfico 5
        elif int(opcao) == 5:
            exec(open('Grafico5-Vendas_Publisher.py').read())

        # Grafico 6
        elif int(opcao) == 6:
            exec(open('Grafico6-Medias.py').read())

        # Sair
        elif int(opcao) == 0:
            op_valida = False
            exibir = False
