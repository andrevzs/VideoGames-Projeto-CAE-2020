# VideoGames-Projeto-CAE-2020
# Easter Egg

# Criado por:
# Andre Vinicius Zicka Schmidt
# Eduardo Scaburi Costa Barros
# Pedro Eduardo Galvan Moreira
# <https://github.com/andrezicka/VideoGames-Projeto-CAE-2020>

# Codigo criado com base no site < edureka.co >

pygame.init()  # Inicializa os modulos do PyGame

# Cores
amarelo = (255, 189, 105)
branco = (236, 236, 236)
vermelho = (255, 99, 99)
fundo = (34, 40, 49)

# Dimensoes da janela
tela_l = 800
tela_a = 800

tela = pygame.display.set_mode((tela_l, tela_a))  # Definicao da janela
pygame.display.set_caption('Easter egg')  # Nome da janela

clock = pygame.time.Clock()  # Relogio que trava os fps

# Ints para a cobra e para a comida
tamanho     = 10
velocidade  = 15

# Fonte usada pra exibir texto
fonte = pygame.font.SysFont("consolas", 25)
fonte_pontos = pygame.font.SysFont("consolas", 26)


# Funcao que exibe os pontos
def pontuacao(pontos):
    # Qual o valor da pontuacao?
    valor = fonte_pontos.render("Pontos: " + str(pontos), True, amarelo)
    tela.blit(valor, [5, 10])  # Exibe a pontuacao na posição definida (x, y)


# Funcao que cria a cobra
def cobra(tamanho_cobra, lista_cobra):
    for x in lista_cobra:
        # Cobra desenhada na tela com a cor branca, nas posicoes da lista x e com o tamanho de 10
        pygame.draw.rect(tela, branco, [x[0], x[1], tamanho_cobra, tamanho_cobra])


# Funcao que cria mensagens
def message(msg, cor):
    mesg = fonte.render(msg, True, cor)
    tela.blit(mesg, [tela_l / 6, tela_a / 3])


# Loop de execucao do jogo, sem ele os eventos nao aconteceriam e o jogo fecharia automaticamente na hora que abrisse
def game_loop():
    game_over = False
    game_close = False

    # Posicoes iniciais da cobra
    x1 = tela_l / 2
    y1 = tela_a / 2

    # Mudanca na posicao da cobra
    x1_change = 0
    y1_change = 0

    lista_cobra = []
    compr_cobra = 1  # Comprimento da cobra

    # Posicoes aleatorias para surgir comida pra cobra
    foodx = round(random.randrange(0, tela_l - tamanho) / 10.0) * 10.0
    foody = round(random.randrange(0, tela_a - tamanho) / 10.0) * 10.0

    # Enquanto o jogador nao tiver perdido
    while not game_over:
        # Se o jogador perder
        while game_close:
            tela.fill(fundo)
            message('Voce Perdeu! Aperte R-Jogar de Novo ou S-Sair', vermelho)
            pontuacao(compr_cobra - 1)  # Pontuacao calculada o tempo inteiro
            pygame.display.update()  # A tela é atualizada

            # Loop que le os eventos que estao sendo executados
            for event in pygame.event.get():
                # Se o jogador apertar alguma tecla
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Se o botao de fechar janela for clicado
                game_over = True
            if event.type == pygame.KEYDOWN:  # Se o jogador apertar alguma tecla
                if event.key == pygame.K_LEFT:  # Se a tecla for a setinha esquerda
                    x1_change = -tamanho
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # Se for a setinha direita
                    x1_change = tamanho
                    y1_change = 0
                elif event.key == pygame.K_UP:  # Se for a setinha pra cima
                    y1_change = -tamanho
                    x1_change = 0
                elif event.key == pygame.K_DOWN:  # Se for a setinha pra baixo
                    y1_change = tamanho
                    x1_change = 0

        # Se a cobra encostar em algum limite da tela
        if x1 >= tela_l or x1 < 0 or y1 >= tela_a or y1 < 0:
            game_close = True

        # O movimento é aplicado na cobra
        x1 += x1_change
        y1 += y1_change

        # Cor do fundo da tela
        tela.fill(fundo)

        # Comidas sao criadas
        pygame.draw.rect(tela, amarelo, [foodx, foody, tamanho, tamanho])

        # Essa parte é responsavel pelo aumento do tamanho da cobra
        cabeca_cobra = [x1, y1]
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > compr_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_close = True

        cobra(tamanho, lista_cobra)
        pontuacao(compr_cobra - 1)

        pygame.display.update()

        # Somar pontos se a cobra comer
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, tela_l - tamanho) / 10.0) * 10.0
            foody = round(random.randrange(0, tela_a - tamanho) / 10.0) * 10.0
            compr_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()


game_loop()
