from heuristics import evaluate
from board import check_winner, make_move, possible_moves
from conf import WHITE, BLACK
from minimax import if_won


def alphabeta(board, d, alpha, beta, maxim, heuristic, nodes):
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

    best_move = None
    best_val = -float("inf") if maxim else float("inf")

    for move in moves:
        value, _ = alphabeta( make_move(board, move), d - 1, alpha, beta, not maxim, heuristic, nodes )

        if maxim:
            if value > best_val:
                best_val = value
                best_move = move

            alpha = max(alpha, best_val)

        else:
            if value < best_val:
                best_val = value
                best_move = move

            beta = min(beta, best_val)

        if beta <= alpha:
            break

    return best_val, best_move