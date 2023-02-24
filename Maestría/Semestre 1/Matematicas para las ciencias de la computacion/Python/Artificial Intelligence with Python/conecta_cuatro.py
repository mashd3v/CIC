# Librerias necesarias
import numpy as np
from easyAI import TwoPlayersGame, Human_Player, AI_Player, \
        Negamax, SSS

# La clase GameController tendra todas las funciones necesarias para jugar
class GameController(TwoPlayersGame):
    def __init__(self, players, board = None):
        # Definiendo los jugadores        
        self.players = players

        # Defininendo la configuracion del tablero
        self.board = board if (board != None) else (
            np.array([[0 for i in range(7)] for j in range(6)]))

        # Definiendo quien empezara el juego
        self.nplayer = 1

        # Definiendo las posiciones
        self.pos_dir = np.array([[[i, 0], [0, 1]] for i in range(6)] +
                 [[[0, i], [1, 0]] for i in range(7)] +
                 [[[i, 0], [1, 1]] for i in range(1, 3)] +
                 [[[0, i], [1, 1]] for i in range(4)] +
                 [[[i, 6], [1, -1]] for i in range(1, 3)] +
                 [[[0, i], [1, -1]] for i in range(3, 7)])


    # Definiendo los posibles movimientos
    def possible_moves(self):
        return [i for i in range(7) if (self.board[:, i].min() == 0)]


    # Definiendo como hacer un movimiento
    def make_move(self, column):
        line = np.argmin(self.board[:, column] != 0)
        self.board[line, column] = self.nplayer


    # Mostrar el estado actual
    def show(self):
        print('\n' + '\n'.join(
                ['0 1 2 3 4 5 6', 13 * '-'] +
                [' '.join([['.', 'O', 'X'][self.board[5 - j][i]]
                for i in range(7)]) for j in range(6)]))


    # Definiendo como se ve la condicion de perdida
    def loss_condition(self):
        for pos, direction in self.pos_dir:
            streak = 0
            while (0 <= pos[0] <= 5) and (0 <= pos[1] <= 6):
                if self.board[pos[0], pos[1]] == self.nopponent:
                    streak += 1
                    if streak == 4:
                        return True
                else:
                    streak = 0
                pos = pos + direction
        return False


    # Verificar si el juego ya ha acabado
    def is_over(self):
        return (self.board.min() > 0) or self.loss_condition()


    # Computar el score
    def scoring(self):
        return -100 if self.loss_condition() else 0


if __name__ == '__main__':
    # Definir los algoritmos que se estaran utilizando
    algo_neg = Negamax(5)
    algo_sss = SSS(5)

    # Empezar el juego
    game = GameController([AI_Player(algo_neg), AI_Player(algo_sss)])
    game.play()

    # Mostrar en pantalla el resultado
    if game.loss_condition():
        print('\nPlayer', game.nopponent, 'wins.')
    else:
        print("\nIt's a draw.")