class Node:
  def __init__(self,key):
    self.id = key
    self.empty=True
    self.North=True
    self.East=True
    self.South=True
    self.West=True

  def getId(self):
    return self.id