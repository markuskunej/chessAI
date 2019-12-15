from chessPlayer import *

def gameIsOver(board, player):
   pos = GetPlayerPositions(board, player)
   for p in pos:
      if GetPieceLegalMoves(board, p, False) != []:
         return False
   return True

factor = -1
player = 10
board = genBoard()
while gameIsOver(board,player) == False:

   print(printBoard(board))
   if player == 10:
      print("WHITE'S TURN")
   elif player == 20:
      print("BLACK'S TURN")
   illeg = True
   position = 0
   user_move = 0
   while illeg:
      position = int(input("Enter the position of the piece you want to move: "))
      if (position > 63) or (position <0):
         print("That position is not on the board!")
         continue
      elif board[position] == 0:
         print("That position is empty!")
         continue
      elif (board[position] < player) or (board[position] > player + 5):
         print("That's not your piece!")
         continue
      
      user_move = int(input("Enter the position where you want to move the piece: "))
      
      legal = GetPieceLegalMoves(board,position, False)
      
      for move in legal:
         if move == user_move:
            illeg = False

      if illeg:
         print("That was an illegal move!")

   board[user_move] = board[position]
   board[position] = 0

   factor *= -1
   player = player + (10*factor)

if (player == 10) and isInCheck(board,player):
   print("Black Wins")
elif (player == 20) and isInCheck(board,player):
   print("White Wins")
else:
   print("Stalemate!")




   

