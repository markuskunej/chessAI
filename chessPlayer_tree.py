from chessPlayer_queue import *

class tree:
   def __init__(self):
      self.store = [[[0,0],0.0],[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      return True

   def Get_LevelOrder(self):
      out = []
      x = Queue()
      x.enqueue(self.store)
      while x.empty() == False:
         r = x.dequeue()
         out = out + [r[0]]
         for i in r[1]:
            x.enqueue(i.store)

      return out


