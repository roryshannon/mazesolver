class Node:
  def __init__(self,key): #the initial values added for the node, the ID which is sent from the main class when creating the graph, and the NESW values i talked about in the main class
    self.id = key
    self.empty=True # again another variable i declared as it could have been useful but was not eventually used due to complications and issues
    self.North=True
    self.East=True
    self.South=True
    self.West=True
    
    self.visited = False
    self.explored = False

  def getId(self): #a simple getter
    return self.id
  
  def get_walls(self): #passed to the graph class which is where it is called from in main for example
    print(f"Node {self.id} has a wall North:{self.North}, has a wall West:{self.West}, has a wall East:{self.East}, has a wall south:{self.South}")
    return self.North, self.West, self.East, self.South 