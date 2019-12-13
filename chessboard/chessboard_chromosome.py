from chessboard.chessboard_state import ChessboardState


class ChessboardChromosome:

    state: ChessboardState
    sequence: list

    def __init__(self, state=None, sequence=None):
        if state is not None:
            self.state = state
            self.sequence = []
            for i, j in state.queen_positions:
                self.sequence.append(i)

        elif sequence is not None:
            self.sequence = sequence
            queen_positions = []
            for i in range(ChessboardState.n):
                queen_positions.append((sequence[i], i))
            self.state = ChessboardState(queen_positions=queen_positions)

        else:
            self.state = ChessboardState.random_state_one_per_col()
            self.sequence = []
            for i, j in self.state.queen_positions:
                self.sequence.append(i)

    def fitness(self):
        return 1.0/(1 + self.state.get_attacking_count())

    def __lt__(self, other):
        assert isinstance(other, ChessboardChromosome)
        return self.state.get_attacking_count() < other.state.get_attacking_count()

    def __eq__(self, other):
        assert isinstance(other, ChessboardChromosome)
        return self.sequence == other.sequence