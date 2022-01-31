import time
from node import Node

class Tremauxs:
    def __init__(self):
        self.name = "tremaux"
        self.visited = []
        self.explored = []
        self.degrees = 0
        self.stack = []
               
    def set_terminal_squares(self, start, end):
        self.start_square = start
        self.end_square = end   
    
    def set_ROW(self, ROW):
        self.ROW = ROW    
    
    def set_direction(self):
        
        
        if self.degrees == 0:
            self.forward = - self.ROW
            self.left = -1
            self.right = +1
            self.compass = "North"
            
            
        if self.degrees == 90:
            self.forward = -1
            self.left = + self.ROW
            self.right = - self.ROW
            self.compass = "West"
            
            
        if self.degrees == 180:
            self.forward = + self.ROW
            self.left = +1
            self.right = -1
            self.compass = "South"
            
            
        if self.degrees == 270:
            self.forward = +1
            self.left = - self.ROW
            self.right = + self.ROW
            self.compass = "East"          
     
    def set_current_square(self, current):
        self.current_square = current #setting as zero to first test get available squares
        #means the square/ node the wall follower is in is updated 
        
    def set_edges(self, edges):
        self.edges = edges
        
    def get_available_moves(self):
        
        self.connections = self.edges[self.current_square]
        
        
        return self.connections
    

    def hmm(self):
        
        if self.current_square + self.forward in self.connections:
            print("moving forward") #so the follower should go forward
            
            self.current_square = self.current_square + self.forward
            self.visited.append(self.current_square)
            self.connections = self.get_available_moves()               
            
            
        elif self.current_square + self.right in self.connections:
            print("moving right") #kinda irrelevant unless there is no move forward
            self.current_square = self.current_square + self.right
            self.visited.append(self.current_square)
            self.connections = self.get_available_moves()
            
            self.degrees += - 90
            if self.degrees < 0:
                self.degrees = 270 #circle for the degrees
            self.set_direction() 
        
    
        elif self.current_square + self.left in self.connections:
            print("moving left") 
            self.current_square = self.current_square + self.left
            self.visited.append(self.current_square)
            self.connections = self.get_available_moves()
            
            self.degrees += 90
            if self.degrees > 270:
                self.degrees = 0 #resetting degrees to 0 when a full circle has been completed
            self.set_direction()
            
        else:
            print("dead end!, retracing steps!")
            self.degrees += 180
            if self.degrees > 270:
                self.degrees = 0 #resetting degrees to 0 when a full circle has been completed
            self.set_direction()
     
      
    def go(self):
        self.tremauxs(self.visited,self.edges,self.start_square)  
           
    def tremauxs(self,visited,graph,node):
        #DFS lol
          #function for dfs
        if node == self.end_square:
            print(node)
            print("solution found!")
            return node
        if node not in visited:
            print (node)
            visited.append(node)
            for neighbour in graph[node]:
                self.tremauxs(visited, graph, neighbour)


        
                    
                
                    
                
            
            
            
            
                         
                 
                
                
            
                
                                   
                                   
