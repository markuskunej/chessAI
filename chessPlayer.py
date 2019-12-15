from chessPlayer_tree import *

def chessPlayer(board, player):
   if len(board) != 64:
      return [False, [], [], []]
   if not ((player == 10) or (player == 20)):
      return [False, [], [], []]
   generated = genPossible(board, player, 3, 0, 0, -10000.0, 10000.0  )
   candidateMoves = []
   bestMove = []
   for moves in generated.store[1]:
      candidateMoves += [moves.store[0]]
   if player == 10:
      maxE = -9999
      for move in generated.store[1]:
         if move.store[0][1] > maxE:
            maxE = move.store[0][1]
            bestMove = [move.store[0][0][0], move.store[0][0][1]]

   else:
      minE = 9999
      for move in generated.store[1]:
         if move.store[0][1] < minE:
            minE = move.store[0][1]
            bestMove = [move.store[0][0][0], move.store[0][0][1]]

   evalTree = generated.Get_LevelOrder()
   move = bestMove
   return [True, move, candidateMoves,evalTree]

def genPossible(board, player, depth, old, new, alpha, beta):
   root = tree()
   root.store[0][0][0] = old
   root.store[0][0][1] = new

   if depth == 0:
      root.store[0][1] = evalBoard(board)
      return root

   if player == 10:
      maxE = -9999.0
      for move in genMoves(board, player):
         temp_board = updateBoard(board, move[0], move[1])
         child = genPossible(temp_board, switch(player), depth - 1, move[0], move[1], alpha, beta)
         root.AddSuccessor(child)
         if child.store[0][1] > maxE:
            maxE = child.store[0][1]
         alpha = max(alpha,maxE)
         if beta <= alpha:
            break
      
      root.store[0][1] = maxE
   
   else:
      minE = 9999.0
      for move in genMoves(board, player):
         temp_board = updateBoard(board, move[0], move[1])
         child = genPossible(temp_board, switch(player), depth - 1, move[0], move[1], alpha, beta)
         root.AddSuccessor(child)
         if child.store[0][1] < minE:
            minE = child.store[0][1]
         beta = min(beta,minE)
         if beta <= alpha:
            break
      root.store[0][1] = minE


   return root
 
def genMoves(board, player):
   accum = []
   for piece in GetPlayerPositions(board, player):
      for move in GetPieceLegalMoves(board, piece, False):
         accum += [[piece, move]]

   return accum 
   

def updateBoard(board, piece, move):
   temp_board = list(board)
   temp_board[move] = temp_board[piece]
   temp_board[piece] = 0
   
   return temp_board
      
def switch(player):
   if player == 10:
      return 20
   else:
      return 10
def updateEval(player, root):
   if player == 10:
      maxE = -9999
      for subT in root.store[1]:
         if subT.ev > maxE:
            maxE = subT.ev
            
      return maxE

   else:
      minE = 9999
      for subT in root.store[1]:
         if subT.ev < minE:
            minE = subT.ev

      return minE

def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1


def getScore(board,pos):
   pawnEvalBlack = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0, 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0, 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5, 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,  0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,  0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]

   pawnEvalWhite = list(reversed(pawnEvalBlack))

   knightEval = [

        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]

   bishopEvalBlack = [
     -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
     -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
     -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
     -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
     -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
     -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
     -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
     -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

   bishopEvalWhite = list(reversed(bishopEvalBlack))

   rookEvalBlack = [
      0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
      0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
      0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]

   rookEvalWhite = list(reversed(rookEvalBlack));
   
   evalQueen = [
     -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
     -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
     -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
     -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
      0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
     -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
     -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
     -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

   kingEvalBlack = [

     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
     -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
      2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ,
      2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]

   kingEvalWhite = list(reversed(kingEvalBlack))

   if board[pos] == 10:
      return 10.0 + pawnEvalWhite[pos]
   if board[pos] == 20:
      return 10.0 + pawnEvalBlack[pos]
   if board[pos] == 11 or board[pos] == 21:
      return 30.0 + knightEval[pos]
   if board[pos] == 12:
      return 30.0 + bishopEvalWhite[pos]
   if board[pos] == 22:
      return 30.0 + bishopEvalBlack[pos]
   if board[pos] == 13:
      return 50.0 + rookEvalWhite[pos]
   if board[pos] == 23:
      return 50.0 + rookEvalBlack[pos]
   if board[pos] == 14 or board[pos] == 24:
      return 90.0 + evalQueen[pos]
   if board[pos] == 15:
      return 900.0 + kingEvalWhite[pos]
   if board[pos] == 25:
      return 900.0 + kingEvalBlack[pos]


def evalBoard(board):
   whiteSum = 0
   blackSum = 0
   white = GetPlayerPositions(board,10)
   for pos in white:
      whiteSum += getScore(board,pos)
   black = GetPlayerPositions(board,20)
   for pos in black:
      blackSum += getScore(board,pos)
   return whiteSum-blackSum


def genBoard():
   r=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63

      r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
      r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
      r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*3] = i+getPiece("king")
      else:
         r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*4] = i+getPiece("king")

      for j in range(0,8):
         r[shift+factor*(j+8)] = i+getPiece("pawn")

   return r

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

def GetPlayerPositions(board,player):
   W = 10
   B = 20
   if (player!=W) and (player!=B):
      return []
   else:
      x0=zip(board,range(0,64,1))
      x1=filter(lambda x : ((x[0]-player) < W) and ((x[0]-player) >= 0), x0)
      return list(map(lambda x:x[1],x1))

def isOnBoard(pos):
   if (pos >= 0) and (pos <= 63):
      return True
   else:
      return False

def isOccupiedByWhite(board, pos):
   if board[pos] > 9 and board[pos]<16:
      return True
   else:
      return False

def isOccupiedByBlack(board, pos):
   if board[pos]>19 and board[pos]<26:
      return True
   else:
      return False

def isSameTeam(board,pos1,pos2):
   if (isOccupiedByWhite(board, pos1) and isOccupiedByWhite(board, pos2)) or (isOccupiedByBlack(board, pos1) and isOccupiedByBlack(board,pos2)):
      return True
   else:
      return False

def isOppTeam(board, pos1, pos2):
   if (isOccupiedByWhite(board, pos1) and isOccupiedByBlack(board, pos2)) or (isOccupiedByBlack(board, pos1) and isOccupiedByWhite(board,pos2)):
      return True
   else:
      return False

def isPositionUnderThreat(board,position,player,check):
   if player == 10:
      opp = 20
   elif player == 20:
      opp = 10
   else:
      return False

   pieces = GetPlayerPositions(board,opp)
   
   for pos in pieces:
      for move in GetPieceLegalMoves(board,pos,check):
         if move == position:
            return True

   return False

def isInCheck(board, player):
   positions = GetPlayerPositions(board, player)
   
   for pos in positions:
      if (board[pos] == 15) or (board[pos] == 25):
         king = pos
   
   if isPositionUnderThreat(board, king, player, True):
      return True
   else:
      return False
      
def GetWhitePawnMoves(pos):
   nr = pos % 8
   nl = 7 - (pos % 8)
   accum = []
   if isOnBoard(pos+8):
      accum += [pos+8]
   if isOnBoard(pos+7) and nr > 0:
      accum += [pos+7]
   if isOnBoard(pos+9) and nl > 0:
      accum += [pos+9]

   return accum

def GetBlackPawnMoves(pos):
   nr = pos % 8
   nl = 7 - (pos % 8)
   accum = []
   if isOnBoard(pos-8):
      accum += [pos-8]
   if isOnBoard(pos-7) and nl > 0:
      accum += [pos-7]
   if isOnBoard(pos-9) and nr > 0:
      accum += [pos-9]

   return accum
 
def GetKnightMoves(pos):
   nr = pos % 8
   nl = 7 - (pos % 8)
   moves = []
   accum = []
   if nr > 0:
      moves += [pos-17, pos+15]
   if nr > 1:
      moves += [pos+6, pos-10]
   if nl>0:
      moves += [pos-15, pos+17]
   if nl>1:
      moves += [pos+10,pos-6]

   for x in moves:
      if isOnBoard(x):
         accum += [x]

   return accum

def GetBishopMoves(board, pos):
   nr = pos % 8
   nl = 7 - (pos % 8)
   accum=[]
   
   ul = pos
   ll = pos
   ur = pos
   lr = pos
   for i in range(0,nr,1):
      ur += 7
      lr -= 9
      if isOnBoard(lr):
         #check if blocked by own pieces
         if isSameTeam(board,pos,lr):
            lr = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,lr):  
            accum += [lr]
            lr = 500
         else:
            accum += [lr]
      if isOnBoard(ur):
         #check if blocked by own pieces
         if isSameTeam(board,pos,ur):
            ur = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,ur): 
            accum += [ur]
            ur = 500
         else:
            accum += [ur]

   for i in range(0,nl,1):
      ul += 9
      ll -= 7
      if isOnBoard(ul):
         #check if blocked by own pieces
         if isSameTeam(board,pos,ul):
            ul = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,ul):
            accum += [ul]
            ul = 500
         else:
            accum += [ul]
      if isOnBoard(ll):
         #check if blocked by own pieces
         if isSameTeam(board,pos,ll): 
            ll = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,ll):
            accum += [ll]
            ll = 500
         else:
            accum += [ll]
   
   return accum

def GetRookMoves(board,pos):
   nl = pos % 8
   nr = 7 - (pos % 8)
   nd = pos // 8
   nu = 7 - (pos // 8)
   #print nl,nr,nd,nu
   accum=[]
   l=r=u=d=pos
   for i in range(0,nl,1):
      l -= 1
      if isOnBoard(l):
         #check if blocked by own pieces
         if isSameTeam(board,pos,l):
            l = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,l):
            accum += [l]
            l = 500
         else:
            accum += [l]

   for i in range(0,nr,1):
      r += 1
      if isOnBoard(r):
         #check if blocked by own pieces
         if isSameTeam(board,pos,r):
            r = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,r):
            accum += [r]
            r = 500
         else:
            accum += [r]
 

   for i in range(0,nd,1):
      d -= 8
      if isOnBoard(d):
          #check if blocked by own pieces
         if isSameTeam(board,pos,d):
            d = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,d):
            accum += [d]
            d = 500
         else:
            accum += [d]

   for i in range(0,nu,1):
      u += 8
      if isOnBoard(u):
         #check if blocked by own pieces
         if isSameTeam(board,pos,u):
            u = 500
         #check if blocked by opponent's piece
         elif isOppTeam(board,pos,u):
            accum += [u]
            u = 500
         else:
            accum += [u]

   return accum

def GetQueenMoves(board,pos):
   return GetRookMoves(board,pos) + GetBishopMoves(board,pos)

def GetKingMoves(pos):
   accum = GetWhitePawnMoves(pos) + GetBlackPawnMoves(pos)
   nr = pos % 8
   nl = 7 - (pos % 8)
   if isOnBoard(pos+1) and nl > 0:
      accum += [pos+1]
   if isOnBoard(pos-1) and nr > 0:
      accum += [pos-1]

   return accum

def GetPieceLegalMoves(board, position,check):
   if position>63 or position<0:
      return[]
   
   accum = []
   player = 0
   piece = board[position]

   if piece == 10:
      player = 10
      moves = GetWhitePawnMoves(position)
      i = 1
      for x in moves:
         if i == 1:
            if board[x] == 0:
               accum += [x]
         else:
            if isOccupiedByBlack(board,x):
               accum += [x]
         i += 1

   elif piece == 20:
      player = 20
      moves = GetBlackPawnMoves(position)
      i = 1
      for x in moves:
         if i == 1:
            if board[x] == 0:
               accum += [x]
         else:
            if isOccupiedByWhite(board, x):
               accum += [x]
         i += 1

   elif piece == 11:
      player = 10
      moves = GetKnightMoves(position)
      for x in moves:
         if not isOccupiedByWhite(board,x):
            accum += [x]

   elif piece == 21:
      player = 20
      moves = GetKnightMoves(position)
      for x in moves:
         if not isOccupiedByBlack(board,x):
            accum += [x]
   
   elif piece == 12:
      player = 10
      accum = GetBishopMoves(board,position)

   elif piece == 22:
      player = 20
      accum = GetBishopMoves(board,position)

   elif piece == 13:
      player = 10
      accum = GetRookMoves(board,position)

   elif piece == 23:
      player = 20
      accum = GetRookMoves(board,position)

   elif piece == 14:
      player = 10
      accum = GetQueenMoves(board,position)

   elif piece == 24:
      player = 20
      accum = GetQueenMoves(board,position)

   elif piece == 15:
      player = 10
      moves = GetKingMoves(position)
      for x in moves:
         if not isSameTeam(board,position,x):
            accum += [x]

   elif piece == 25:
      player = 20
      moves = GetKingMoves(position)
      for x in moves:
         if not isSameTeam(board,position,x):
            accum += [x] 
   else:
      return []
 
   legal = []

   for move in accum:
      temp_board = list(board)
      temp_board[move] = piece
      temp_board[position] = 0
      if check:
         legal += [move]
      elif not isInCheck(temp_board, player):
         legal += [move]

   return legal


