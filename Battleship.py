from random import randint

def create_board(board):
  for x in range(0,5):
    board.append(["."] * 5)
  print_board
  return board

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def dupe_check(row1, col1, row2, col2):
  ship_row2 = random_row(board)
  ship_col2 = random_col(board)
  while row1 == row2 and col1 == col2:
    ship_row2 = random_row(board)
    ship_col2 = random_col(board)
  return (ship_row2, ship_col2)

def stats(board, row1, col1, row2, col2):
  global sunk
  global won
  global lost
  if board[row1][col1] == "X" and board[row2][col2] == "X":
    sunk += 2
    won += 1
  elif board[row1][col1] == "X" or board[row2][col2] == "X":
    sunk += 1
    lost += 1
  else:
    lost += 1
  stats = float(won) / (won + lost)
  print "You've sunk", sunk, "ships!"
  print "You've won", won, "games and lost", lost, "games."
  print "Your victory rate is", stats
  return (sunk, won, lost)

board = []

create_board(board)
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

ship_row2 = random_row(board)
ship_col2 = random_col(board)
    
dupe_check(ship_row, ship_col, ship_row2, ship_col2)

sunk = 0
won = 0
lost = 0

def play(board, ship_row, ship_col, ship_row2, ship_col2):
  print "Find both battleships!"
  print "Choose a column and row, 1 - 5"
  replay = "y"

  while replay == "y":
    board = []
    create_board(board)

    print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)

    ship_row2 = random_row(board)
    ship_col2 = random_col(board)
    
    dupe_check(ship_row, ship_col, ship_row2, ship_col2)
    
    ship1 = 0
    
    for turn in range(8):
      if turn >= 1:
        print
        print "Guess again!"
    
      print "Turn", turn + 1
      print
  
      try:
        guess_row = int(raw_input("Guess Row: ")) - 1
      except ValueError:
        print "That wasn't even a number. Let's just go with 2."
        guess_row = 2
      try:
        guess_col = int(raw_input("Guess Col: ")) - 1
      except ValueError:
        print "That wasn't even a number. Let's just go with 2."
        guess_col = 2
      print
  
      if guess_row == ship_row and guess_col == ship_col or \
         guess_row == ship_row2 and guess_col == ship_col2:
        print "Congratulations! You sank my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)
        if turn == 7:
          if board[ship_row][ship_col] == "X" and \
          board[ship_row2][ship_col2] == "X":
            print
            print "You win!"
            print_board(board)
          else:
            print "Game Over"
            print "You didn't find my second ship!"
            print "The correct answers were"
            print ship_row, ",", ship_col
            print "and"
            print ship_row2, ",", ship_col2
            print
            board[ship_row][ship_col] = "X"
            board[ship_row2][ship_col2] = "X"
            print_board(board)
            break
        elif ship1 == 1:
          break
        else:
          print "Find the second ship!"
          ship1 = 1
      else:
        if guess_row not in range(5) or \
          guess_col not in range(5):
          print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "O":
          print( "You guessed that one already." )
        else:
          if abs(guess_row - ship_row) <= 1 and \
          abs(guess_col - ship_col) <= 1 and \
          abs(guess_row - ship_row2) <= 1 and \
          abs(guess_col - ship_col2) <= 1:
            print "They've got you surrounded!"
            board[guess_row][guess_col] = "2"
          elif abs(guess_row - ship_row) <= 1 and \
          abs(guess_col - ship_col) <= 1 or \
          abs(guess_row - ship_row2) <= 1 and \
          abs(guess_col - ship_col2) <= 1:
            print "So close!"
            board[guess_row][guess_col] = "1"
          else:
            print "Not even close!"
            board[guess_row][guess_col] = "O"
        if (turn == 7):
          print "Game Over"
          print "The correct answers were"
          print ship_row, ",", ship_col
          print "and"
          print ship_row2, ",", ship_col2
          print
          if board[ship_row][ship_col] == "." or \
          board[ship_row][ship_col] == "1" or \
          board[ship_row][ship_col] == "2" or \
          board[ship_row][ship_col] == "0":
            board[ship_row][ship_col] = "x"
          if board[ship_row2][ship_col2] == "." or \
          board[ship_row2][ship_col2] == "0" or \
          board[ship_row2][ship_col2] == "1" or \
          board[ship_row2][ship_col2] == "2":
            board[ship_row2][ship_col2] = "x"
        print_board(board)
    
    stats(board, ship_row, ship_col, ship_row2, ship_col2)
    
    replay = raw_input("Would you like to play again? (y/n) ")
    if replay != "y" and replay != "n":
      print "I'm sorry, I need a yes or a no."
      replay = raw_input("Would you like to play again? (y/n)")
    if replay == "n":
      print "See you next time!"
      
play(board, ship_row, ship_col, ship_row2, ship_col2)
