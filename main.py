# main.py

# Setup Board
board = ["--"] * 8

for i in range(len(board)):
    board[i] = ["--"] * 8


# Display the board to the terminal
def print_board(board):
    i = 8
    for row in board:
        print(f"{i}:", end=" ")
        i -= 1
        for col in row:
            print(col, end=" ")
        print()
        print()
    print("   A  B  C  D  E  F  G  H")

print_board(board)
