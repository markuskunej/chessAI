from chessPlayer import *
from random import randint
import time
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
   if player == 20:
      print("Black Turn")
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

   elif player == 10:
      '''accum = []
      L = GetPlayerPositions(board,player)
      for i in range (0,len(L),1):
         accum += [[L[i],[]]]
         print(accum)         
         moves = GetPieceLegalMoves(board,L[i],False)
         print(moves)
         for move in moves:
            if not isPositionUnderThreat(board, move, player,False):
               accum[i][1] += [move]
      
      index = randint(0,len(accum)-1)
      position = accum[index][0]
      print(position)
      user_move = accum[index][1][randint(0,len(accum[index][1])-1)]
      print(user_move)'''
      startTime = time.time()
      compGen = chessPlayer(board, player)
      elapsedTime = time.time() - startTime
      print(compGen[1])
      print(compGen[2])
      
      position = compGen[1][0]
      user_move = compGen[1][1]
      print(elapsedTime)
      
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




   

