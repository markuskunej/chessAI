class Queue:
   def __init__(self):
      self.list = []

   def enqueue(self, val):
      self.list = self.list + [val]
      return 0

   def dequeue(self):
      if len(self.list) == 0:
         return False
      val = self.list[0]
      self.list = self.list[1:]
      return val

   def empty(self):
      if len(self.list) == 0:
         return True
      else:
         return False

