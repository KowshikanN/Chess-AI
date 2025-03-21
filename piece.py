import abc

class Piece(abc.ABC):
    def __init__(self, color, board, position):
        assert color in ('w', 'b')
        self.color = color
        self.board = board
        self.position = position

    @abc.abstractmethod
    def next(self):
        return []

    def generate_sliding_moves(self, directions):
        """
        Helps to generate the sliding type moves for pieces like the Bishop, Rook, and Queen.

        """
        x, y = self.position
        boards = []
        for directionX, directionY in directions:
            newX, newY = x + directionX, y + directionY
            while 0 <= newX <= 7 and 0 <= newY <= 7:  # Makes sure it stays within bounds
                theTarget = self.board[newX, newY]
                if theTarget is None:  # Makes sure it is an empty square
                    new_board = self.board.copy()
                    new_board.board[(newX, newY)] = self.__class__(self.color, new_board, (newX, newY))
                    del new_board.board[(x, y)]
                    boards.append(new_board)
                elif theTarget.color != self.color:  # Capture logic for getting ememy piece
                    new_board = self.board.copy()
                    new_board.capture(newX, newY)
                    new_board.board[(newX, newY)] = self.__class__(self.color, new_board, (newX, newY))
                    del new_board.board[(x, y)]
                    boards.append(new_board)
                    break  # Stops the sliding move in this direction
                else:  # looks for a friendly piece, which will make it stop sliding
                    break
                newX, newY = newX + directionX, newY + directionY
        return boards


class Bishop(Piece):
    def next(self):
        directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]  # Dictionairy of all diagonal directions
        return self.generate_sliding_moves(directions)

class King(Piece):
    def next(self):
        """
        Generates all the valid moves for the King.
        """
        x, y = self.position
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        boards = []
        for directionX, directionY in directions:
            newX, newY = x + directionX, y + directionY
            if 0 <= newX <= 7 and 0 <= newY <= 7:  # Check if it is within the bounds
                theTarget = self.board[newX, newY]
                if theTarget is None or theTarget.color != self.color:
                    new_board = self.board.copy()  # Copies the board using the copy function
                    new_board.capture(newX, newY)
                    new_board.board[(newX, newY)] = King(self.color, new_board, (newX, newY))
                    del new_board.board[(x, y)]
                    boards.append(new_board)
        return boards


class Knight(Piece):
    def next(self):
        x, y = self.position
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                 (2, 1), (1, 2), (-1, 2), (-2, 1)]  # Dictionairy for the L-shaped moves
        boards = []
        for directionX, directionY in moves:
            newX, newY = x + directionX, y + directionY
            if 0 <= newX <= 7 and 0 <= newY <= 7:  # Checks if it is within the boundries
                theTarget = self.board[newX, newY]
                if theTarget is None or theTarget.color != self.color:
                    new_board = self.board.copy()
                    new_board.capture(newX, newY)
                    new_board.board[(newX, newY)] = Knight(self.color, new_board, (newX, newY))
                    del new_board.board[(x, y)]
                    boards.append(new_board)
        return boards


class Peon(Piece):
    def next(self):
        x, y = self.position
        direction = 1 if self.color == 'w' else -1  # Logic for making sure that the White moves up and Black moves down
        boards = []

        # Logic for the forward movement of the peon
        newX, newY = x, y + direction
        if 0 <= newY <= 7 and self.board[newX, newY] is None:  # Makes sure that it can only move forward if the square is empty
            new_board = self.board.copy()

            # Apply Contagion if not already applied
            if not new_board.contagion_applied:
                new_board.contagion()

            if newY == 7 and self.color == 'w' or newY == 0 and self.color == 'b':  # Promotion logic for peon once it makes it to the other side
                new_board.board[(newX, newY)] = Knight(self.color, new_board, (newX, newY))
            else:
                new_board.board[(newX, newY)] = Peon(self.color, new_board, (newX, newY))
            del new_board.board[(x, y)]
            boards.append(new_board)

        # Capture logic for the peon 
        for directionX in [-1, 1]:
            newX, newY = x + directionX, y + direction
            if 0 <= newX <= 7 and 0 <= newY <= 7:
                theTarget = self.board[newX, newY]
                if theTarget and theTarget.color != self.color:  # Captures the enemy piece
                    new_board = self.board.copy()

                    # Apply Contagion if not already applied
                    if not new_board.contagion_applied:
                        new_board.contagion()

                    if newY == 7 and self.color == 'w' or newY == 0 and self.color == 'b':  # Promotion on capture if it makes it to the other side
                        new_board.board[(newX, newY)] = Knight(self.color, new_board, (newX, newY))
                    else:
                        new_board.board[(newX, newY)] = Peon(self.color, new_board, (newX, newY))
                    del new_board.board[(x, y)]
                    boards.append(new_board)

        return boards


class Queen(Piece):
    def next(self):
        directions = [(-1, -1), (1, -1), (-1, 1), (1, 1),  # Dictionairy for the diagonal moves
                      (0, -1), (0, 1), (-1, 0), (1, 0)]    # Dictionairy for the vertical and horizontal moves
        return self.generate_sliding_moves(directions)


class Rook(Piece):
    def next(self):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Dictionairy for the vertical and horizontal moves
        return self.generate_sliding_moves(directions)
