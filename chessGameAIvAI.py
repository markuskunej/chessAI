import chessPlayer
import chessPlayerB
from random import randint
import time
def gameIsOver(board, player):
   pos = chessPlayer.GetPlayerPositions(board, player)
   for p in pos:
      if chessPlayer.GetPieceLegalMoves(board, p, False) != []:
         return False
   return True

factor = -1
player = 10
board = chessPlayer.genBoard()
while gameIsOver(board,player) == False:
   print(chessPlayer.printBoard(board))
   if player == 10:
      print("Black's TURN")
      r = input("Press Enter")
      startTime = time.time()
      compGen = chessPlayerB.chessPlayer(board, player)
      elapsedTime = time.time() - startTime
      print(elapsedTime)
      position = compGen[1][0]
      user_move = compGen[1][1]
      print(compGen)


   elif player == 20:
      print("White's Turn")
      r = input("Press Enter")
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
      compGen = chessPlayer.chessPlayer(board, player)
      elapsedTime = time.time() - startTime
      print(elapsedTime)
      
      position = compGen[1][0]
      user_move = compGen[1][1]
      print(compGen)
      
   board[user_move] = board[position]
   board[position] = 0

   factor *= -1
   player = player + (10*factor)

if (player == 10) and chessPlayer.isInCheck(board,player):
   print("Black Wins")
elif (player == 20) and chessPlayer.isInCheck(board,player):
   print("White Wins")
else:
   print("Stalemate!")




   

