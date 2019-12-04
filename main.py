from file_io import read_config, write_config
from chessboard.chessboard_state import ChessboardState
from algorithms.abstract_solver import AbstractSolver
from algorithms.hill_climbing_solver import HillClimbingSolver

if __name__ == '__main__':
    initial_config = read_config('input.txt')

    state = ChessboardState(initial_config)
    # state.print_chessboard()

    # print("Neighbors:")
    # for s in state.neighbors():
    #     s.print_chessboard()

    # print(len(state.neighbors()))

    a = HillClimbingSolver()