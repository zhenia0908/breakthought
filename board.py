import copy
from conf import ROWS, WHITE, BLACK, EMPTY, LAST

def print_board(board):
    for row in board:
        print(" ".join(row))

def make_board():
    board = []
    for i in range(ROWS):
        if i < 2:
            board.append([BLACK] * ROWS)
        elif i > 5:
            board.append([WHITE] * ROWS)
        else:
            board.append([EMPTY] * ROWS)
    return board

def possible_moves(board, player):
    moves = []
    direction = -1 if player == WHITE else 1

    diagonals = [-1, 1]

    for row in range(ROWS):
        for col in range(ROWS):
            if board[row][col] != player:
                continue

            next_row = row + direction
            if not (0 <= next_row < ROWS):
                continue

            if board[next_row][col] == EMPTY:
                moves.append(((row, col), (next_row, col)))
            for offset in diagonals:
                next_col = col + offset
                if 0 <= next_col < ROWS:
                    if board[next_row][next_col] != player:
                        moves.append( ((row, col), (next_row, next_col)))
    return moves

def make_move(board, move):
    new = copy.deepcopy(board)

    (i, j), (ni, nj) = move
    for x in range(ROWS):
        for y in range(ROWS):
            if new[x][y] == LAST:
                new[x][y] = EMPTY
    new[ni][nj] = new[i][j]
    new[i][j] = LAST  
    return new


def check_winner(board):
    if WHITE in board[0]:
        return WHITE
    if BLACK in board[-1]:
        return BLACK
    return None