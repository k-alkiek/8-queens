from random import randrange


class ChessboardState:
    """
    Encapsulates the logic of the game

    Args:
        chessboard (list): 2D list of characters representing the chessboard.
                            Q denotes a queen and # denotes an empty cell
    Attributes:
        queen_positions (frozenset): set of tuples representing locations of queens in the chessboard
    """
    queen_positions: frozenset
    n = 8

    def __init__(self, chessboard=None, queen_positions=None):
        if chessboard is not None:
            self.queen_positions = frozenset()
            self.init_queen_positions(chessboard)
        elif queen_positions is not None:
            self.queen_positions = frozenset(queen_positions)

    def init_queen_positions(self, chessboard):
        config = []
        for i in range(ChessboardState.n):
            for j in range(ChessboardState.n):
                if chessboard[i][j] == 'Q':
                    config.append((i, j))
        self.queen_positions = frozenset(config)

    def get_attacking_count(self):
        collisions = 0
        for i1, j1 in self.queen_positions:
            for i2, j2 in self.queen_positions:
                if i1 == i2 and j1 == j2:  # Skip if same queen
                    continue
                if i1 == i2 or j1 == j2 or i1 - j1 == i2 - j2 or i1 + j1 == i2 + j2:
                    collisions += 1
        return collisions // 2

    def neighbors(self):
        neighbors_queen_positions = []
        for pos in self.queen_positions:
            for new_pos in self.moves_from_position(*pos):
                new_queen_positions = set(self.queen_positions)
                new_queen_positions.remove(pos)
                new_queen_positions.add(new_pos)
                neighbors_queen_positions.append(new_queen_positions)
        return [ChessboardState(queen_positions=frozenset(nqp)) for nqp in neighbors_queen_positions]

    def moves_from_position(self, i_pos, j_pos):
        moves = []

        # Add vertical and horizontal moves, exclude current position
        moves += list(
            zip([i for i in range(ChessboardState.n) if i != i_pos], [j_pos for _ in range(ChessboardState.n - 1)]))
        moves += list(
            zip([i_pos for _ in range(ChessboardState.n - 1)], [j for j in range(ChessboardState.n) if j != j_pos]))

        # Add diagonal moves, exclude current position
        moves += list(zip(range(i_pos + 1, ChessboardState.n), range(j_pos + 1, ChessboardState.n)))  # bottom left
        moves += list(zip(range(i_pos + 1, ChessboardState.n), range(j_pos - 1, -1, -1)))  # bottom right
        moves += list(zip(range(i_pos - 1, -1, -1), range(j_pos + 1, ChessboardState.n)))  # top left
        moves += list(zip(range(i_pos - 1, -1, -1), range(j_pos - 1, -1, -1)))  # bottom right

        # Remove moves that overlap with another queen
        moves = [m for m in moves if m not in self.queen_positions]
        return moves

    def get_chessboard(self):
        chessboard = [['#' for _ in range(ChessboardState.n)] for _ in range(ChessboardState.n)]
        for i, j in self.queen_positions:
            chessboard[i][j] = 'Q'
        return chessboard

    def print_chessboard(self):
        for row in self.get_chessboard():
            print(row)
        print()

    def __lt__(self, other):
        assert isinstance(other, ChessboardState)
        return self.get_attacking_count() < other.get_attacking_count()

    def __hash__(self):
        return self.queen_positions.__hash__()

    def __eq__(self, other):
        assert isinstance(other, ChessboardState)
        return self.queen_positions == other.queen_positions

    """
        Returns a state with one queen per column
    """
    @classmethod
    def random_state_one_per_col(cls, seed=None):
        queen_positions = []
        for i in range(cls.n):
            queen_positions.append((randrange(0, cls.n), i))

        state = ChessboardState(queen_positions=queen_positions)
        return state
