class Node:
  def __init__(self,key):
    self.id = key
    self.empty=True
    self.North=True
    self.East=True
    self.South=True
    self.West=True
    
    self.visited = False
    self.explored = False

  def getId(self):
    return self.id
  
  def get_walls(self):
    print(f"Node {self.id} has a wall North:{self.North}, has a wall West:{self.West}, has a wall East:{self.East}, has a wall south:{self.South}")
    return self.North, self.West, self.East, self.South 