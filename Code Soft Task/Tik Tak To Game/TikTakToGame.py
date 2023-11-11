def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = "X"

        while True:
            print_board(board)
            try:
                row = int(input(f"Player {player}, enter row (0, 1, 2): "))
                col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = player
                if check_win(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                else:
                    player = "O" if player == "X" else "X"
            else:
                print("Invalid move. Try again.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
