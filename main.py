from PyQt5 import QtWidgets

from algorithms.ga_solver import GASolver
from ui.main_window import MainWindow
import sys

from file_io import read_config, write_config
from chessboard.chessboard_state import ChessboardState

if __name__ == '__main__':
    pass
    initial_config = read_config('input.txt')

    state = ChessboardState(initial_config)
    state.print_chessboard()
    print(len(state.neighbors()));

    # GUI
    # app = QtWidgets.QApplication(sys.argv)
    # main = MainWindow()
    # main.setWindowTitle("8 Queens")
    # main.show()
    # sys.exit(app.exec_())
