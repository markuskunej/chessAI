class tree:
   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      return True

   def Print_DepthFirst(self,level=0):
      print("   " * level + str(self.store[0]))
      if (len(self.store[1]) != 0):
         for tree in self.store[1]:
            tree.Print_DepthFirst(level + 1)
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


