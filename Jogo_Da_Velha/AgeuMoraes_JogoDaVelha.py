
import numpy as np  # Bibliotecas para manipular matrizes

# Função que cria os tabuleiros de várias dimensões
def create_game_board(size):
    # Criando o tabuleiro inicialmente vazio
    return np.full((size, size), " ")


# Função que exibe o tabuleiro com numerações na parte de cima e das laterais para guiar o jogador
def show_game_board(game_board):
    # Váriavel que retorna o tamanho do tabuleiro como uma tupla
    size = game_board.shape[0]

    # Exibe números na parte de cima que facilitam a visualização do jogo
    print("   " + "   ".join(str(i) for i in range(1, size+1)))

    # Traz o tamanho do tabuleiro para retorna símbolos e números que deixam o código mais intuitivo
    for i in range(size):
        # Exibe as barras que dividem as colunas e colocam números na lateral para facilitar a visualizçação do jogo
        print(f"{i+1}  " + " | ".join(game_board[i]))
        # Traços que dividem as linhas
        if i < size - 1:
            print("  " + "-" * (4 * size - 1))


# Função das jogadas dos jogadores
def make_move(game_board, player, position):
    # Define a posição de jogada do jogador seja ele quem for
    line, column = position
    # Verifica se a posição está disponível e permite a jogada do jogador qualquer
    if game_board[line-1][column-1] == " ":
        game_board[line-1][column-1] = player
        return True
    return False


# Função que verifica quem venceu
def checks_winner(game_board, player):
    # Váriavel que retorna o tamanho do tabuleiro como uma tupla
    size = game_board.shape[0]
    # Verificar linhas
    for i in range(size):
        # Verifica a vitória linha por linha e retorna verdadeiro se isso acontecer
        if np.all(game_board[i] == player):
            return True
    # Verificar colunas
    for j in range(size):
        # Verifica a vitória coluna por coluna e retorna verdadeiro se isso acontecer
        if np.all(game_board[:, j] == player):
            return True
    # Verificar diagonais. Na diagonal secundária o tabuleiro inverte, sendo lido também
    if np.all(np.diagonal(game_board) == player) or np.all(np.diagonal(np.fliplr(game_board)) == player):
        return True
    return False


# Função que irá rodar o jogo quando for chamada
def play():
    # Pede para informar o tamanho do tabuleiro
    size = int(input("Informe o tamanho do tabuleiro: "))
    # Cria o tabuleiro conforme o tamanho dele
    game_board = create_game_board(size)
    # Definem os jogadores dentro de uma lista
    players = ["X", "O"]
    # Contador
    current_player = 0

    # Fica em iteração em quanto for verdadeiro
    while True:
        # Chama a função que cria o tabuleiro
        show_game_board(game_board)
        # Como o jogador atual é 0, que começa é o X
        player = players[current_player]
        # Pede para o jogador informar a linha e a coluna
        position = input(f"Jogador '{player}', informe a posição (linha, coluna): ")
        # Transforma a string posicao em uma tupla de inteiros separados por vírgula através do split, e o map aplica
        # o int a cada posição
        position = tuple(map(int, position.split(",")))

        try:
            # Verfica cada passo para se considerar vitória para o jogador
            if make_move(game_board, player, position):
                if checks_winner(game_board, player):
                    show_game_board(game_board)
                    print(f"Parabéns! O jogador '{player}' venceu!")
                    break
                # Usa uma função que verifica se tem algum espaço não nulo na matriz, se não houver, ela retorna nulo
                # Executando assim, a condicional que define o empate
                elif np.count_nonzero(game_board == " ") == 0:
                    show_game_board(game_board)
                    print("Empate!")
                    break
                # Se nada ocorreu, o jogo passa para o próximo jogador
                current_player = (current_player + 1) % 2
            # Se nenhuma das condicionais anteriores executaram, então a posição será inválida
            else:
                print("Posição inválida. Tente novamente.")
        
        except:
            print("Ocorreu algum problema!! Tente novamente!!")


# Função para separar, de maneira mais bonita, as coisas no terminal
def separate():
    print("=" * 95)


separate()
print("ESSE JOGO DA VELHA FOI FEITO PARA JOGAR DE DUAS PESSOAS\n")
print("VOCÊ TEM QUE INFORMAR O TAMANHO DO TABULEIRO ")
print("EXEMPLO: (3, 5, 7, 9,..., n)\n")
print("O 'X' COMEÇA O JOGO\n")
print("ESCOLHA A POSIÇÃO QUE DESEJAR")
print("VOCÊ PODE SE GUIAR PELOS NÚMEROS NA LATERAL E NA PARTE DE CIMA")
print("OS VALORES DA POSIÇÃO QUE VOCÊ DESEJA JOGAR, TEM QUE SER SEPARADOS POR ','")
print("EXEMPLO DE JOGADA: 2,3\n")
print("BOA SORTE! VOCÊ VAI PRECISAR;)\n")
separate()
# Colocando o jogo para rodar
play()
