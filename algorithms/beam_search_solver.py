import time
from heapq import nsmallest

from algorithms.abstract_solver import AbstractSolver
from chessboard.chessboard_state import ChessboardState
from chessboard.chessboard_state_node import ChessboardStateNode


class BeamSearchSolver(AbstractSolver):
    def __init__(self, k=1):
        self.k = k
        self.start_time = 0
        self.end_time = 0
        self.expanded_count = 0
        self.depth = 0

    def solve(self):
        self.start_time = time.time()
        # Initial random fringe with k states
        fringe = [ChessboardStateNode(ChessboardState.random_state_one_per_col()) for _ in range(self.k)]
        explored = set()

        while fringe[0].cost() > 0:
            self.depth += 1
            new_fringe = []
            for node in fringe:
                if node in explored:
                    continue

                self.expanded_count += 1
                explored.add(node)
                for child in node.neighbors():
                    if child not in explored:
                        new_fringe.append(child)
            fringe = nsmallest(self.k, new_fringe)

        self.end_time = time.time()
        return fringe[0].chessboard_state

    def get_running_time(self):
        return self.end_time - self.start_time

    def get_cost(self):
        return self.depth

    def get_expanded_count(self):
        return self.expanded_count

    def get_best_k(self):
        pass