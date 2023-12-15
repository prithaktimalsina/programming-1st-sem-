def int_to_reverse_binary(integer_value):
    binary_string = ""
def print_board(board):
    for row in board:
        print(' '.join(row))
        print('-' * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([all([spot != ' ' for spot in row]) for row in board])

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = 0

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {player_turn % 2 + 1}'s turn (row, col): ").strip().split())
        
        if board[row][col] != ' ':
            print("That spot is taken. Try again.")
            continue

        board[row][col] = 'X' if player_turn % 2 == 0 else 'O'
        
        if is_winner(board, board[row][col]):
            print_board(board)
            print(f"Player {player_turn % 2 + 1} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player_turn += 1

if __name__ == "__main__":
    main()