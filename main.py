from PyQt5 import QtWidgets

from algorithms.ga_solver import GASolver
from algorithms.csp_solver import CSPSolver
from algorithms.hill_climbing_solver import HillClimbingSolver
from chessboard.chessboard_state_node import ChessboardStateNode
from ui.main_window import MainWindow
import sys

from file_io import read_config, write_config
from chessboard.chessboard_state import ChessboardState

if __name__ == '__main__':
    # pass
    initial_config = read_config('input2.txt')

    state = ChessboardState(initial_config)
    state.print_chessboard()

    # csp = CSPSolver()
    # csp.solve(state)
    # print("Number steps to the final solution =", csp.get_cost())
    # csp.final_sol.print_chessboard()
    # print("Expanded node count =", csp.get_expanded_count())
    # print("Execution time in milliseconds =", csp.get_running_time())

    hill = HillClimbingSolver()
    hill.solve(ChessboardStateNode(state), 'sa')
    print("Number steps to the final solution =", hill.get_cost())
    hill.get_final_solution().print_chessboard()
    print("Number of attacks in the final solution =", hill.conflictions_count)
    print("Expanded node count =", hill.get_expanded_count())
    print("Execution time in milliseconds =", hill.get_running_time())
    #
    # print(len(state.neighbors()));

    # GUI
    # app = QtWidgets.QApplication(sys.argv)
    # main = MainWindow()
    # main.setWindowTitle("8 Queens")
    # main.show()
    # sys.exit(app.exec_())
