from random import randint

board = []

for x in range(0, 5):
  board.append([" ~ "] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

for turn in range(10):
  if turn < 9:
    print("Turn", turn + 1, ", you've got", 9 - turn, "left.") 
  else:
    print("Last turn!")

  guess_col = int(input("Guess Column: "))
  guess_row = int(input("Guess Row: "))
  

  if guess_row == ship_row and guess_col == ship_col:
    print("*** Congratulations! You sank my battleship! ***")
    board[guess_row-1][guess_col-1] = " x "
    print_board(board)
    break
  else:
    if guess_row not in range(1,6) or \
      guess_col not in range(1,6):
      print("Oops, that's out of bounds.")
    elif board[guess_row-1][guess_col-1] == " o ":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row-1][guess_col-1] = " o "
    print_board(board)
    if turn == 9:
      print("Game Over.")