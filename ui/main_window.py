from ast import literal_eval
from functools import partial

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QSizePolicy, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from chessboard.chessboard_state import ChessboardState
from file_io import read_config, write_config
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    n = 8

    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initial stuff
        self.chessboard = [['#' for _ in range(MainWindow.n)] for _ in range(MainWindow.n)]
        self.chessboard_btns = []
        self.ui.centralwidget.setStyleSheet("background-color: #CBCBCB")
        self.ui.menubar.setStyleSheet("background-color: #A8A8A8")
        self.create_chessboard()

        # Connect up the buttons.
        self.ui.resetButton.clicked.connect(self.reset_chessboard)
        self.ui.actionLoad.triggered.connect(self.load_file)
        self.ui.actionSave.triggered.connect(self.save_file)

        # Populate chessboard grid

    def create_chessboard(self):

        first_tile_in_row_light = True
        for i in range(MainWindow.n):
            tile_light = first_tile_in_row_light
            for j in range(MainWindow.n):
                btn = QPushButton()
                cbk = partial(self.chess_tile_clicked, btn)
                btn.clicked.connect(cbk)
                btn.setIconSize(QSize(50, 50))
                btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                if tile_light:
                    btn.setStyleSheet("border-radius: 0px; background-color: #E8EBEF")
                else:
                    btn.setStyleSheet("border-radius: 0px; background-color: #7D8796")

                tile_light = not tile_light

                self.ui.gridLayout.addWidget(btn, i, j)
            first_tile_in_row_light = not first_tile_in_row_light

    def chess_tile_clicked(self, btn):
        index = self.ui.gridLayout.indexOf(btn)
        i = index // MainWindow.n
        j = index % MainWindow.n

        if self.chessboard[i][j] == '#':
            self.chessboard[i][j] = 'Q'
            btn.setIcon(QIcon('./ui/queen-tile.png'))
        elif self.chessboard[i][j] == 'Q':
            self.chessboard[i][j] = '#'
            btn.setIcon(QIcon())

    def reset_chessboard(self):
        s = ChessboardState(self.chessboard)
        self.chessboard = [['#' for _ in range(MainWindow.n)] for _ in range(MainWindow.n)]
        for i in range(self.ui.gridLayout.count()):
            pass
            btn = self.ui.gridLayout.itemAt(i).widget()
            btn.setIcon(QIcon())

    def refresh_chessboard(self):
        for i in range(MainWindow.n):
            for j in range(MainWindow.n):
                index = i*MainWindow.n + j
                btn = self.ui.gridLayout.itemAt(index).widget()
                if self.chessboard[i][j] == '#':
                    btn.setIcon(QIcon())
                elif self.chessboard[i][j] == 'Q':
                    btn.setIcon(QIcon('./ui/queen-tile.png'))

    def load_file(self):
        file, _ = QFileDialog.getOpenFileName(QFileDialog(), 'Open File')
        if file:
            self.chessboard = read_config(file)
            self.refresh_chessboard()

    def save_file(self):
        file, _ = QFileDialog.getSaveFileName(QFileDialog(), 'Save')
        if file:
            write_config(file, self.chessboard)
