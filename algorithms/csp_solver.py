from algorithms.abstract_solver import AbstractSolver
from chessboard.chessboard_state import ChessboardState
from random import randint
import time
"""
    Implementation of the Min-Conflicting algorithm with CSP.

    Parameter:
        initial_chessboard_state: a ChessboardState instance.
"""
n = 8


class CSPSolver(AbstractSolver):

    steps_count = 0
    expanded_count = 0
    execution_time = 0
    final_sol = None

    def solve(self, initial_chessboard_state):
        # Structure: each column should contain only one queen
        prev_expanded = []
        start_time = time.time()
        current_state, positions = self.get_chessboard_and_positions(initial_chessboard_state)
        while True:
            print("Current state #attacks =", current_state.get_attacking_count())
            current_state.print_chessboard()
            last_cost = current_state.get_attacking_count()
            if last_cost == 0:
                self.final_sol = current_state
                break
            positions = self.heuristic_move(positions)
            current_state = ChessboardState(queen_positions=positions)
            # while any(current_state.__eq__(x) for x in prev_expanded):
            #     positions = self.heuristic_move(positions)
            #     current_state = ChessboardState(queen_positions=positions)
            self.expanded_count += 1
            prev_expanded.append(current_state)
            if last_cost == current_state.get_attacking_count():        # local optima
                print("--- Local Optima ---")
                positions = self.random_move(positions)
                current_state = ChessboardState(queen_positions=positions)
                while any(current_state.__eq__(x) for x in prev_expanded):
                    positions = self.random_move(positions)
                    current_state = ChessboardState(queen_positions=positions)
                self.expanded_count += 1
                prev_expanded.append(current_state)
                last_cost = current_state.get_attacking_count()
            else:
                last_cost = current_state.get_attacking_count()
            self.steps_count += 1
        end_time = time.time()
        self.execution_time = end_time - start_time
        return self.final_sol

    def get_running_time(self):
        return int(round(self.execution_time * 1000))

    def get_cost(self):
        return self.steps_count

    def get_expanded_count(self):
        return self.expanded_count

    def get_chessboard(self, positions):
        chessboard = [['#' for _ in range(n)] for _ in range(n)]
        for i, j in positions:
            chessboard[i][j] = 'Q'
        return chessboard

    def get_attacking_count(self, x, y, positions):
        collisions = 0
        for x1, y1 in positions:
            if x == x1 and y == y1:  # Skip if same queen
                continue
            if x == x1 or y == y1 or x - y == x1 - y1 or x + y == x1 + y1:
                collisions += 1
        return collisions

    def get_chessboard_and_positions(self, chessboard):
        positions = [x for x in chessboard.queen_positions]
        invalid = False
        cols = [False for i in range(n)]
        for i in range(n):
            if cols[positions[i][1]]:
                invalid = True
                for j in range(n):
                    if not cols[j]:
                        positions[i] = (positions[i][0], j)
                        cols[j] = True
                        break
            else:
                cols[positions[i][1]] = True
        if invalid:
            configuration = [['#' for _ in range(n)] for _ in range(n)]
            for i, j in positions:
                configuration[i][j] = 'Q'
            board = ChessboardState(configuration, positions)
            return board, positions
        else:
            return chessboard, positions

    def heuristic_move(self, positions):
        # Ordering: choose the queen with the max conflicts count and move it to the row which causes minimum
        # conflicts count.
        max_conflict_count = -1
        queen_pos = 0
        max_x, max_y = positions[0]
        for i in range(n):
            x, y = positions[i]
            conflict_count = self.get_attacking_count(x, y, positions)
            if conflict_count > max_conflict_count:
                max_conflict_count = conflict_count
                max_x, max_y = positions[i]
                queen_pos = i
        min_conflict_count = 100
        min_row = 0
        for i in range(n):
            conflict_count = self.get_attacking_count(i, max_y, positions)
            if conflict_count < min_conflict_count:
                min_conflict_count = conflict_count
                min_row = i
        # Variable Assignment
        positions[queen_pos] = (min_row, max_y)
        return positions

    def random_move(self, positions):
        x, y = randint(0, 7), randint(0, 7)
        for i in range(n):
            x1, y1 = positions[i]
            if y1 == y:
                positions[i] = (x, y)
                break
        return positions