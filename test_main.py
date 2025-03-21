import sys
from board import Board

if __name__ == '__main__':
    board = Board.from_string(sys.stdin.read())
    for i, new_board in enumerate(board.next()):
        with open(f'board.{i:03d}', 'w') as f:
            f.write(new_board.to_string())
