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
     
      
    def go(self):
        end = self.tremauxs(self.visited,self.edges,self.start_square)  
        
    def stop(self):
        print("thanks for using my code")
        time.sleep(100000000)
           
    def tremauxs(self,visited,graph,node):
        #DFS lol
          #function for dfs
        if node == self.end_square:
            print("final node,",node,"reached")
            print("solution found!")
            self.stop()
        elif node not in visited:
            print ("moving to", node)
            visited.append(node)
            for neighbour in graph[node]:
                self.tremauxs(visited, graph, neighbour)


        
                    
                
                    
                
            
            
            
            
                         
                 
                
                
            
                
                                   
                                   
