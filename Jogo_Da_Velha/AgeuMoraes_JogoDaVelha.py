
import numpy as np  # Libraries for manipulating arrays


class TicTacToe:
    
    def __init__(self):
        self.separate()
        print("ESSE JOGO DA VELHA FOI FEITO PARA JOGAR DE DUAS PESSOAS\n")
        print("VOCÊ TEM QUE INFORMAR O TAMANHO DO TABULEIRO ")
        print("EXEMPLO: (3, 5, 7, 9,..., n)\n")
        print("O 'X' COMEÇA O JOGO\n")
        print("ESCOLHA A POSIÇÃO QUE DESEJAR")
        print("VOCÊ PODE SE GUIAR PELOS NÚMEROS NA LATERAL E NA PARTE DE CIMA")
        print("OS VALORES DA POSIÇÃO QUE VOCÊ DESEJA JOGAR, TEM QUE SER SEPARADOS POR ','")
        print("EXEMPLO DE JOGADA: 2,3\n")
        print("BOA SORTE! VOCÊ VAI PRECISAR;)\n")
        self.separate()

    # Function that creates n-dimensional game tables
    def create_game_board(self, size):
        # Criando o tabuleiro inicialmente vazio
        return np.full((size, size), " ")


    # Function that shows game table with numbers above and on the sides to guide players
    def show_game_board(self, game_board):
        # Variable that returns the table number as a tuple
        size = game_board.shape[0]

        # Shows numbers above that make it easier to see the game
        print("   " + "   ".join(str(i) for i in range(1, size+1)))

        # With the size of the game table create a table using symbols
        for i in range(size):
            # Shows bars that divide the columns and places numbers next to them to make the game easier to see
            print(f"{i+1}  " + " | ".join(game_board[i]))
            # Traits that divide lines
            if i < size - 1:
                print("  " + "-" * (4 * size - 1))


    # Function of the plays of the players
    def make_move(self, game_board, player, position):
        # Defines the player's playing position, regardless of who they are
        line, column = position
        # Checks if there is an open position and allows moves by any player
        if game_board[line-1][column-1] == " ":
            game_board[line-1][column-1] = player
            return True
        return False


    # Function that checks who the winner is
    def checks_winner(self, game_board, player):
        # Variable that returns the value from the game table as a tuple
        size = game_board.shape[0]
        # Checks the lines
        for i in range(size):
            # Checks for win line by line and returns True if it does
            if np.all(game_board[i] == player):
                return True
        # Checks the columns
        for j in range(size):
            # Checks for win column by column and returns True if it does
            if np.all(game_board[:, j] == player):
                return True
        # Check the diagonals. On the secondary diagonal, the board is inverted, and is also read
        if np.all(np.diagonal(game_board) == player) or np.all(np.diagonal(np.fliplr(game_board)) == player):
            return True
        return False


    # Function that will run the game as be called
    def play(self):
        # Asks to inform the size of the game table
        size = int(input("Informe o tamanho do tabuleiro: "))
        # Creates the game table of the according to size him
        game_board = self.create_game_board(size)
        # Defines players in a list
        players = ["X", "O"]
        # counter
        current_player = 0

        # Will be iterating as long as it is true
        while True:
            # Call function that creates the game table
            self.show_game_board(game_board)
            # As the first player is 0, X is the one who starts
            player = players[current_player]
            # Ask to the player inform the line and the column
            position = input(f"Jogador '{player}', informe a posição (linha, coluna): ")
            # Transforms the position string on a tuple of ints split to commas through the "split" function, and the map apply the int the each position
            position = tuple(map(int, position.split(",")))

            try:
                # Checks each step to consider a player's victory
                if self.make_move(game_board, player, position):
                    if self.checks_winner(game_board, player):
                        self.show_game_board(game_board)
                        print(f"Parabéns! O jogador '{player}' venceu!")
                        break
                    # Use the function that checks if there is any non-null place in the array, if not, it returns null
                    # Then, executing the conditional that defines the tie
                    elif np.count_nonzero(game_board == " ") == 0:
                        self.show_game_board(game_board)
                        print("Empate!")
                        break
                    # If this doesn't happen, the game will go to the next level
                    current_player = (current_player + 1) % 2
                # If none of the conditionals are executed, then invalid position
                else:
                    print("Posição inválida. Tente novamente.")
            
            except:
                print("Ocorreu algum problema!! Tente novamente!!")


    # Function to beautifully divide things in the terminal
    def separate(self):
        print("=" * 95)
        

tic_tac_toe = TicTacToe()
tic_tac_toe.play() # Initializes the game
