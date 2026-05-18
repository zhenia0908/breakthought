from heuristics import evaluate
from board import check_winner, possible_moves, make_move
from conf import WHITE, BLACK

def if_won(winner):
 if winner == WHITE:
        return 10000, None
 if winner == BLACK:
        return -10000, None
 return None



def minimax(board, d, maxim, heuristic, nodes):
    nodes[0] += 1
    winner = check_winner(board)
    result = if_won(winner)

    if result is not None:
        return result
    
    if d == 0:
        return evaluate(board, heuristic), None
    
    player = WHITE if maxim else BLACK
    moves = possible_moves(board, player)

    if not moves:
        return evaluate(board, heuristic), None
    children = []

    for move in moves:
        value, _ = minimax( make_move(board, move), d - 1, not maxim, heuristic, nodes)
        children.append((value, move))

    if maxim:
        return max(children)

    return min(children)