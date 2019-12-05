from chessboard.chessboard_state import ChessboardState


class ChessboardStateNode:
    """
    Represents a node in a search tree. Encapsulates a chessboard state and keeps track of parent and depth

    Attributes:
        chessboard_state (ChessboardState): The chessboard state represented by the node
        parent (ChessboardStateNode): Parent of the node in the search tree
        depth (int): Depth of the node in the search tree
    """
    chessboard_state: ChessboardState
    parent: 'ChessboardStateNode'
    depth: int

    def __init__(self, chessboard_state, parent=None, depth=None):
        self.chessboard_state = chessboard_state
        self.parent = parent
        self.depth = depth if depth is not None else 0

    def neighbors(self):
        neighbor_nodes = []
        for neighbor in self.chessboard_state.neighbors():
            node = ChessboardStateNode(neighbor, self, self.depth + 1)
            neighbor_nodes.append(node)
        return neighbor_nodes

    def cost(self):
        return self.chessboard_state.get_attacking_count()

    def __lt__(self, other):
        assert isinstance(other, ChessboardStateNode)
        return self.cost() < other.cost()

    def __hash__(self):
        return self.chessboard_state.__hash__()

    def __eq__(self, other):
        assert isinstance(other, ChessboardStateNode)
        return self.chessboard_state == other.chessboard_state
