from termios import NOFLSH
import time
import sys
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
        end = self.tremauxs_rec(self.visited,self.edges,self.start_square)
        ##print(f"end is {end}") 
        
    def stop(self):
        input = ("thanks for using my code")
        sys.exit()
        
        
           
    def tremauxs_rec(self,visited,graph,node):
         
        #function for trems
        if node == self.end_square:
            print("final node,",node,"reached")
            print("solution found!")
            #return node
            self.stop()
            
        else:
            print ("moving to", node)
            visited.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    self.tremauxs_rec(visited, graph, neighbour)
        
        
    '''def tremauxs_diff(self):
        stack = []
        
        while self.current_square != self.end_square:
            for neighbour in self.edges[self.current_square]:
                if neighbour not in self.visited:
                    stack.append(neighbour)
            if not self.current_square in self.visited:
              self.visited.append(self.current_square)
            self.current_square = stack.pop()'''
                                          
