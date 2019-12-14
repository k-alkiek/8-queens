from algorithms.abstract_solver import AbstractSolver
from random import randint
import time
from chessboard.chessboard_state import ChessboardState
from chessboard.chessboard_state_node import ChessboardStateNode

"""
    Implementation of the Hill Climbing base algorithm with random restarting on local minimum.

    Parameter:
        initial_chessboard_state: a ChessboardStateNode instance encapsulating the current chessboard state.
"""
n = 8


class HillClimbingSolver(AbstractSolver):
    conflictions_count = float('inf')
    steps_count = 0
    expanded_count = 0
    execution_time = 0
    optimal_sol = None
    RANDOM_RESTART_LIMIT = 10
    prev_expanded_states = []

    def solve(self, initial_chessboard_state, local_optima_solve='rr'):
        min_cost = initial_chessboard_state.cost()
        current_state = initial_chessboard_state
        sideways = []
        rr_count = 0
        start_time = time.time()
        while True:
            print("Current state #attacks =", current_state.cost())
            current_state.chessboard_state.print_chessboard()
            self.prev_expanded_states.append(current_state.chessboard_state)
            if current_state.cost() == 0:
                self.steps_count += current_state.depth
                self.conflictions_count = 0
                self.optimal_sol = current_state.chessboard_state
                break
            changed = False
            for state in current_state.neighbors():
                if state.cost() < min_cost:
                    min_cost = state.cost()
                    current_state = state
                    changed = True
            if not changed:  # no better state and still not global optima --> local optima
                if current_state.cost() < self.conflictions_count:
                    self.conflictions_count = current_state.cost()
                    self.optimal_sol = current_state.chessboard_state
                    self.steps_count += current_state.depth
                if local_optima_solve == 'sa' and len(sideways) > 0:
                    current_state = sideways.pop()
                    min_cost = current_state.cost()
                    print("--- Local Optima --- Use Sideway move")
                else:
                    if rr_count == self.RANDOM_RESTART_LIMIT:
                        break
                    else:
                        current_state = self.random_restart()
                        min_cost = current_state.cost()
                        rr_count += 1
                        print("--- Local Optima #", rr_count, "--- Use random restart")
            else:
                for state in current_state.parent.neighbors():
                    if state.cost() == min_cost and not any(state.chessboard_state.__eq__(x) for x in self.prev_expanded_states):
                        sideways.append(state)
            self.expanded_count += 1
        end_time = time.time()
        self.execution_time = end_time - start_time
        return self.optimal_sol

    def get_running_time(self):
        return int(round(self.execution_time * 1000))

    def get_cost(self):
        return self.steps_count

    def get_expanded_count(self):
        return self.expanded_count

    def random_restart(self):
        configuration = [['#' for _ in range(n)] for _ in range(n)]
        positions = []
        for i in range(n):
            x, y = randint(0, n - 1), randint(0, n - 1)
            if positions.count([x, y]) != 0:
                i -= 1
            else:
                positions.append([x, y])
        for i, j in positions:
            configuration[i][j] = 'Q'
        board = ChessboardState(configuration)
        while any(board.__eq__(e) for e in self.prev_expanded_states):
            configuration = [['#' for _ in range(n)] for _ in range(n)]
            positions.clear()
            for i in range(n):
                x, y = randint(0, n - 1), randint(0, n - 1)
                if positions.count([x, y]) != 0:
                    i -= 1
                else:
                    positions.append([x, y])
            for i, j in positions:
                configuration[i][j] = 'Q'
            board = ChessboardState(configuration)
        return ChessboardStateNode(board)

    def get_final_solution(self):
        return self.optimal_sol
