import time
import sys
from node import Node

class Tremauxs:
    def __init__(self): #initialting base values for the class, a list of visited nodes and its name - just a little nice touch I like to add
        self.name = "tremaux" 
        self.visited = []
               
    def set_terminal_squares(self, start, end): #setter for the start and end squares
        self.start_square = start
        self.end_square = end           
        
    def set_edges(self, edges): #collecting the connections from the graph
        self.edges = edges   
      
    def go(self): #calling the DFS and starting the recursion
        go = self.tremauxs_rec(self.visited,self.edges,self.start_square) #declares var go as the recursive function, this was when I wanted the return value to work
               
    def stop(self): #my solution to the puzzling fault in my recursive depth first search
        input = ("thanks for using my code")
        sys.exit()
                        
    def tremauxs_rec(self,visited,graph,node): #the meat of my tremaix algorithm, a depth first search which goes through my program and keeps moving to the next node until the end node is found
         
        #function for trems
        if node == self.end_square: #the base case / condition which should stop the program
            print("final node,",node,"reached") 
            print("solution found!")
            #return node
            self.stop() # the call to the function whcih actually stops the program
            
        else: #the recursive part of the program
            print ("moving to", node)
            visited.append(node) #adds the node the solver ahs just visited to the visited list
            for neighbour in graph[node]: #moves to the next node or "neighbour"
                if neighbour not in visited: #if it has not been visited yet, it is a valid move 
                    self.tremauxs_rec(visited, graph, neighbour) #so we can go there by setting the current square to "neighbour"
        
        