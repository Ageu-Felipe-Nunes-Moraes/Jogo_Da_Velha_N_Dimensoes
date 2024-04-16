
import numpy as np  # Bibliotecas para manipular matrizes

# Função que cria os tabuleiros de várias dimensões
def criar_tabuleiro(tamanho):
    # Criando o tabuleiro inicialmente vazio
    return np.full((tamanho, tamanho), " ")


# Função que exibe o tabuleiro com numerações na parte de cima e das laterais para guiar o jogador
def exibir_tabuleiro(tabuleiro):
    # Váriavel que retorna o tamanho do tabuleiro como uma tupla
    tamanho = tabuleiro.shape[0]

    # Exibe números na parte de cima que facilitam a visualização do jogo
    print("   " + "   ".join(str(i) for i in range(1, tamanho+1)))

    # Traz o tamanho do tabuleiro para retorna símbolos e números que deixam o código mais intuitivo
    for i in range(tamanho):
        # Exibe as barras que dividem as colunas e colocam números na lateral para facilitar a visualizçação do jogo
        print(f"{i+1}  " + " | ".join(tabuleiro[i]))
        # Traços que dividem as linhas
        if i < tamanho - 1:
            print("  " + "-" * (4 * tamanho - 1))


# Função das jogadas dos jogadores
def fazer_jogada(tabuleiro, jogador, posicao):
    # Define a posição de jogada do jogador seja ele quem for
    linha, coluna = posicao
    # Verifica se a posição está disponível e permite a jogada do jogador qualquer
    if tabuleiro[linha-1][coluna-1] == " ":
        tabuleiro[linha-1][coluna-1] = jogador
        return True
    return False


# Função que verifica quem venceu
def verificar_vitoria(tabuleiro, jogador):
    # Váriavel que retorna o tamanho do tabuleiro como uma tupla
    tamanho = tabuleiro.shape[0]
    # Verificar linhas
    for i in range(tamanho):
        # Verifica a vitória linha por linha e retorna verdadeiro se isso acontecer
        if np.all(tabuleiro[i] == jogador):
            return True
    # Verificar colunas
    for j in range(tamanho):
        # Verifica a vitória coluna por coluna e retorna verdadeiro se isso acontecer
        if np.all(tabuleiro[:, j] == jogador):
            return True
    # Verificar diagonais. Na diagonal secundária o tabuleiro inverte, sendo lido também
    if np.all(np.diagonal(tabuleiro) == jogador) or np.all(np.diagonal(np.fliplr(tabuleiro)) == jogador):
        return True
    return False


# Função que irá rodar o jogo quando for chamada
def jogar():
    # Pede para informar o tamanho do tabuleiro
    tamanho = int(input("Informe o tamanho do tabuleiro: "))
    # Cria o tabuleiro conforme o tamanho dele
    tabuleiro = criar_tabuleiro(tamanho)
    # Definem os jogadores dentro de uma lista
    jogadores = ["X", "O"]
    # Contador
    jogador_atual = 0

    # Fica em iteração em quanto for verdadeiro
    while True:
        # Chama a função que cria o tabuleiro
        exibir_tabuleiro(tabuleiro)
        # Como o jogador atual é 0, que começa é o X
        jogador = jogadores[jogador_atual]
        # Pede para o jogador informar a linha e a coluna
        posicao = input(f"Jogador '{jogador}', informe a posição (linha, coluna): ")
        # Transforma a string posicao em uma tupla de inteiros separados por vírgula através do split, e o map aplica
        # o int a cada posição
        posicao = tuple(map(int, posicao.split(",")))

        try:
            # Verfica cada passo para se considerar vitória para o jogador
            if fazer_jogada(tabuleiro, jogador, posicao):
                if verificar_vitoria(tabuleiro, jogador):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Parabéns! O jogador '{jogador}' venceu!")
                    break
                # Usa uma função que verifica se tem algum espaço não nulo na matriz, se não houver, ela retorna nulo
                # Executando assim, a condicional que define o empate
                elif np.count_nonzero(tabuleiro == " ") == 0:
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break
                # Se nada ocorreu, o jogo passa para o próximo jogador
                jogador_atual = (jogador_atual + 1) % 2
            # Se nenhuma das condicionais anteriores executaram, então a posição será inválida
            else:
                print("Posição inválida. Tente novamente.")
        
        except:
            print("Ocorreu algum problema!! Tente novamente!!")


# Função para separar, de maneira mais bonita, as coisas no terminal
def separar():
    print("=" * 95)


separar()
print("ESSE JOGO DA VELHA FOI FEITO PARA JOGAR DE DUAS PESSOAS\n")
print("VOCÊ TEM QUE INFORMAR O TAMANHO DO TABULEIRO ")
print("EXEMPLO: (3, 5, 7, 9...)\n")
print("O 'X' COMEÇA O JOGO\n")
print("ESCOLHA A POSIÇÃO QUE DESEJAR")
print("VOCÊ PODE SE GUIAR PELOS NÚMEROS NA LATERAL E NA PARTE DE CIMA")
print("OS VALORES DA POSIÇÃO QUE VOCÊ DESEJA JOGAR, TEM QUE SER SEPARADOS POR ','")
print("EXEMPLO DE JOGADA: 2,3\n")
print("BOA SORTE! VOCÊ VAI PRECISAR;)\n")
separar()
# Colocando o jogo para rodar
jogar()
