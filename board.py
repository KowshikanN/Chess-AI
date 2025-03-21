from piece import Bishop, King, Knight, Peon, Queen, Rook


class Board:
    pieces = {
        'B': Bishop,
        'K': King,
        'N': Knight,
        'P': Peon,
        'Q': Queen,
        'R': Rook,
    }

    def __init__(self, board=None, turn=None):
        self.check(board)
        self.board = board or {}
        self.turn = turn
        self.contagion_applied = False

    @classmethod
    def check(cls, board):
        for x, y in board.keys():
            assert 0 <= x <= 7
            assert 0 <= y <= 7

    @classmethod
    def from_string(cls, txt):
        """
        Initializes the board from a string.

        Parameters
        ----------
        txt: str
            The string input to parse.

        Returns
        -------
        result: Board
            The Board object created from the input.
        """
        lines = txt.strip().split('\n')

        # Gets the turn'w' or 'b' from the first line of the file 
        turn, _, _, _ = lines[0].split()

        # Finds the board section that tell us about the positions
        starting_index = lines.index('{') + 1
        ending_index = lines.index('}')

        # Parses through the board one by one manually
        board = {}
        for line in lines[starting_index:ending_index]:
            line = line.strip().rstrip(',')
            if not line:
                continue
            position, piece_str = line.split(':')
            position = position.strip()
            piece_str = piece_str.strip().strip("'")
            x, y = cls.convert_the_position(position)
            color, piece_type = piece_str[0], piece_str[1]
            if piece_type in cls.pieces:  # Checks if the piece is valid within the input
                piece_cls = cls.pieces[piece_type]
                board[(x, y)] = piece_cls(color, None, (x, y))  # Initially sets board to None

        # Creates the Board instance
        new_board_instance = cls(board=board, turn=turn)

        # Links each of the pieces to the board instance created above
        for piece in new_board_instance.board.values():
            piece.board = new_board_instance

        return new_board_instance

    @staticmethod
    def convert_the_position(position):
        """Converts a position on the board into a usable coordinate."""
        x = ord(position[0]) - ord('a')  # Converts the column letter to a coordinate number (X)
        y = int(position[1]) - 1         # Converts the  row number to 0-based index coordinate (Y)
        return x, y

    def __getitem__(self, position):
        return self.board.get(position, None)

    def capture(self, x, y):
        if (x, y) in self.board:
            del self.board[(x, y)]

    def copy(self):
        return Board(self.board.copy(), self.turn)

    def next(self):
        for piece in self.board.values():
            if piece.color == self.turn:
                for board in piece.next():
                    yield board

    def to_string(self):
        board_repr = '{\n'
        for pos, piece in self.board.items():
            x, y = pos
            piece_symbol = next(symbol for symbol, cls in self.pieces.items() if isinstance(piece, cls))
            # This will convert the position coordinates that are generated to a human-readable version
            board_repr += f"  {chr(x + ord('a'))}{y + 1}: '{piece.color}{piece_symbol}',\n"
        board_repr += '}\n'
        return f"{self.turn} 0 0 0\n{board_repr}0\n0\n0\n"