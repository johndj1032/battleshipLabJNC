from random import randint

board = []
for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print((" ").join(row))

print("Play:")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(13):
    guess_row = int(input("Guess Row:"))
    guess_col = int(
        input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print("Ship Sunk")
        break
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print("Not Valid")
        elif(board[guess_row][guess_col] == "X"):
            print("Same Guess")
        else:
            print("Miss")
            board[guess_row][guess_col] = "X"
    turn = turn + 1
    print_board(board)