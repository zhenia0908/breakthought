
from conf import ROWS, WHITE, BLACK, EMPTY
from board import possible_moves

def h1_pawns(board, player):
    score = 0
    for i in range(ROWS):
        for j in range(ROWS):
            if board[i][j] == player:
                score += 1
    return score


def h2_progress(board, player):
    score = 0
    if player == WHITE:
        for i in range(ROWS):
            for j in range(ROWS):
                if board[i][j] == WHITE:
                    score += (ROWS - i)
    else:
        for i in range(ROWS):
            for j in range(ROWS):
                if board[i][j] == BLACK:
                    score += i
    return score

def h3_support(board, player):
    score = 0
    for i in range(ROWS):
        for j in range(ROWS):
            if board[i][j] != player:
                continue
            if player == WHITE:
                back_row = i + 1
            else:
                back_row = i - 1
            if 0 <= back_row < ROWS:
                if j > 0 and board[back_row][j - 1] == player:
                    score += 1
                if j < ROWS - 1 and board[back_row][j + 1] == player:
                    score += 1
    return score

def h4_mobility(board, player):
    return len(possible_moves(board, player))

def h5_combined(board, player):
    pawns = h1_pawns(board, player)
    progress = h2_progress(board, player)
    support = h3_support(board, player)
    mobility = h4_mobility(board, player)
    return (pawns * 100) + (progress * 10) + (support * 2) + (mobility * 1)

def evaluate(board, heuristic):
    if heuristic == 1:
        return h1_pawns(board, WHITE) - h1_pawns(board, BLACK)
    if heuristic == 2:
        return h2_progress(board, WHITE) - h2_progress(board, BLACK)
    if heuristic == 3:
        return h3_support(board, WHITE) - h3_support(board, BLACK)
    if heuristic == 4:
        return h4_mobility(board, WHITE) - h4_mobility(board, BLACK)
    return h5_combined(board, WHITE) - h5_combined(board, BLACK)