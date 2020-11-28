import pandas as pd

vg = pd.read_csv('VideoGames.csv', sep=',')

t = True

print('='*10, 'VIDEOGAMES - Projeto CAE 2020', '='*11)

while t:
    print('=-'*26, '\n'
          '[1] Vendas de Jogos por Região       (Graf. Linhas)\n'
          '[2] Frequência de Notas (Review)     (Graf. Barras)\n'
          '[3] 10 Generos Mais Vendidos         (Graf. Barras)\n'
          '[4] Num. de Jogos por Plataforma     (Graf. Barras)\n'
          '[5] Vendas por Publisher             (Graf. Linhas)\n'
          '[0] Encerrar programa')
    print('~'*52)

    op_valida = False
    while not op_valida:
        opcao = input('Digite uma das opções: ')
        try:
            int(opcao)
            if 0 <= int(opcao) <= 5:
                op_valida = True
            else:
                print('Putz! Só tem 5 opções no menu!\n')
                op_valida = False
        except ValueError:
            print('= Oops... você deve digitar a opção como um número inteiro! =\n')
            op_valida = False

    if op_valida:
        # Gráfico 1
        if int(opcao) == 1:
            print('\nSelecione uma forma de gerar o gráfico:\n'
                  '[1] Para todos os anos\n'
                  '[2] Definir um intervalo de anos')
            tipo_valido = False
            while not tipo_valido:
                tipo = input('Opção: ')
                try:
                    int(tipo)
                    if 1 <= int(tipo) <= 2:
                        tipo_valido = True
                    else:
                        print('-ERRO!- Digite apenas 1 ou 2.\n')
                        tipo_valido = False
                except ValueError:
                    print('= Oops... você deve digitar a opção como um número inteiro! =\n')
                    tipo_valido = False
            if int(tipo) == 1:
                pass  # Executar gráfico pra todos os anos

            if int(tipo) == 2:
                anoi_valido = False
                while not anoi_valido:
                    ano_i = input('Digite o 1º ano:(entre 1977 e 2018) ')
                    try:
                        int(ano_i)
                        if 1977 <= int(ano_i) <= 2018:
                            anoi_valido = True
                        else:
                            print('Ano Inicial deve estar entre 1977 e 2018\n')
                            anoi_valido = False
                    except ValueError:
                        print('O Ano Inicial deve ser digitado como um número inteiro de 4 dígitos.\n')
                        anoi_valido = False

                if anoi_valido:
                    anof_valido = False
                    while not anof_valido:
                        ano_f = input(f'Digite o 2º ano:(entre {ano_i} e 2018) ')
                        try:
                            int(ano_f)
                            if int(ano_i) <= int(ano_f) <= 2018:
                                anof_valido = True
                            else:
                                print(f'Ano Final deve estar entre {ano_i} e 2018\n')
                                anof_valido = False
                        except ValueError:
                            print('O Ano Final deve ser digitado como um número inteiro de 4 dígitos.\n')
                            anof_valido = False

                    if anof_valido:
                        pass  # graf1(ano_i, ano_f)

        # Gráfico 2
        elif int(opcao) == 2:
            pass

        # Gráfico 3
        elif int(opcao) == 3:
            print('\nSelecione uma forma de gerar o gráfico:\n'
                  '[1] Para todos os anos\n'
                  '[2] Definir um intervalo de anos\n'
                  '[3] Ano específico')
            tipo_valido = False
            while not tipo_valido:
                tipo = input('Opção: ')
                try:
                    int(tipo)
                    if 1 <= int(tipo) <= 3:
                        tipo_valido = True
                    else:
                        print('-ERRO!- Digite apenas 1, 2 ou 3.\n')
                        tipo_valido = False
                except ValueError:
                    print('= Oops... você deve digitar a opção como um número inteiro! =\n')
                    tipo_valido = False

                if int(tipo) == 2:
                    anoi_valido = False
                    while not ano_i:
                        ano_i = input('Digite o 1º ano:(entre 1977 e 2018 ')
                        try:
                            int(ano_i)
                            if 1977 <= int(ano_i) <= 2018:
                                anoi_valido = True
                            else:
                                print('Ano Inicial deve estar entre 1977 e 2018\n')
                                anoi_valido = False
                        except ValueError:
                            print('O Ano Inicial deve ser gitiado como um número inteiro de 4 dígitos.\n')
                            anoi_valido = False

                        if anoi_valido:
                            anof_valido = False
                            while not anof_valido:
                                ano_f = input(f'Digite o 2º ano:(entre {ano_i} e 2018) ')
                                try:
                                    int(ano_f)
                                    if int(ano_i) <= int(ano_f) <= 2018:
                                        anof_valido = True
                                    else:
                                        print(f'Ano Final deve estar entre {ano_i} e 2018\n')
                                        anof_valido = False
                                except ValueError:
                                    print('O Ano Final deve ser digitado como um número inteiro de 4 dígitos.')
                                    anof_valido = False

                                if anof_valido:
                                    pass  # graf3(ano_i, ano_f)

                if int(tipo) == 3:
                    ano_valido = False
                    while not ano_valido:
                        op_ano = input('Digite o ano:(entre 1977 e 2018) ')
                        try:
                            int(op_ano)
                            if 1977 <= int(op_ano) <= 2018:
                                op_valida = True
                            else:
                                op_valida = False
                                print('O ano deve estar entre 1977 e 2018!')
                                op_ano = input('Digite o ano: ')
                        except ValueError:
                            print('O ano deve ser digitado como um número inteiro de 4 dígitos.\n')
                            op_valida = False
                            
                    if op_valida:
                        pass  # graf3(op_ano, 0)

        # Gráfico 4
        elif int(opcao) == 4:
            pass

        # Gráfico 5
        elif int(opcao) == 5:
            pass

        # Sair
        elif int(opcao) == 0:
            op_valida = False
            t = False
