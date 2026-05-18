from board import make_board, make_move, print_board, check_winner, possible_moves
from visualization import BoardVisualizer
from minimax import minimax
from alpha_beta import alphabeta
import time
import sys
from conf import WHITE, BLACK


def main():
    board = make_board()

    depth = int(input("Depth: "))
    heuristic = int(input("Choose heuristic (1, 2, 3, 4, 5): "))
    use_alpha_beta = int(input("Choose Alpha-Beta=1 or Minimax=2: "))

    nodes = [0]
    start = time.time()
    viz = BoardVisualizer(rows=8, size=600)

    turn = WHITE
    rounds = 0
    running = True

    while running:

        running = viz.handle_events()
        winner = check_winner(board)
        if winner:
            print("Winner:", winner)
            break

        moves = possible_moves(board, turn)
        if not moves:
           winner = BLACK if turn == WHITE else WHITE
           print("No moves. Winner:", winner)
           break

        print("Round:", rounds)
        maximizing = (turn == WHITE)

        if use_alpha_beta:
            _, move = alphabeta(board, depth, -float("inf"), float("inf"), maximizing, heuristic, nodes )
        else:
            _, move = minimax(board, depth, maximizing, heuristic, nodes )


        if move is None:
          print("No move returned. Game over.")
          break

        board = make_move(board, move)
        viz.draw(board)
        time.sleep(0.3)

        turn = BLACK if turn == WHITE else WHITE
        rounds += 1

    end = time.time()

    print_board(board)
    print(rounds, check_winner(board))

    print(f"Nodes: {nodes[0]}", file=sys.stderr)
    print(f"Time: {end - start:.4f}s", file=sys.stderr)


if __name__ == "__main__":
    main()