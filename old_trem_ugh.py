import time
from node import Node

class Tremauxs:
    def __init__(self):
        self.name = "tremaux"
        self.visited = []
               
    def set_terminal_squares(self, start, end):
        self.start_square = start
        self.end_square = end   
    
    def set_ROW(self, ROW):
        self.ROW = ROW    
    
    def set_direction(self, degrees):
        
        
        self.degrees = degrees
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
        print(f"at {self.current_square} tremuax can move to: {self.connections}")
        
        return self.connections
    
    def mark_as_visited(self):
        self.visited.append(self.current_square)
    
    def deadend(self, degrees):
        #if self.current_square in self.visited: # if there is a dot at one junction?
        degrees += 180 # run the deadend code
        if degrees > 270: #make it circular
            degrees = 0
                
        return degrees
    
    def crossed(self, connections):
        if len(self.connections) > 2:
            return True
        
    def make_move(self):
        degrees = 0
        while self.current_square != self.end_square:
            
            if len(self.connections) > 2:
                for i in range(len(self.connections)):
                    if self.connections[i] not in self.visited:
                        if self.connections[i] == self.current_square - self.forward:
                            print("cant go backwards yet!") 
                            next
                        else:
                            
                            #how to make the move! call the below with a function?
                            self.current_square = self.connections[i]
                        
                            self.visited.append(self.current_square)
                            
                            print(self.visited, self.current_square)
                            
                            #time.sleep(10000)
                            break
                            #print(2)
                
                
                print("all next squares lead nowhere! turning round")
                degrees += 180
                if degrees > 270:
                    degrees = 0
                self.set_direction(degrees)   
                      
            
            else:
                
                
                if self.current_square + self.forward in self.connections:
                    print("moving forward") #so the follower should go forward
                    self.current_square = self.current_square + self.forward
                    self.connections = self.get_available_moves()               
                    
                    
                elif self.current_square + self.right in self.connections:
                    print("moving right") #kinda irrelevant unless there is no move forward
                    self.current_square = self.current_square + self.right
                    self.connections = self.get_available_moves()
                    
                    degrees += - 90
                    if degrees < 0:
                        degrees = 270 #circle for the degrees
                    self.set_direction(degrees) 
                    
                
                elif self.current_square + self.left in self.connections:
                    print("moving left") 
                    self.current_square = self.current_square + self.left
                    self.connections = self.get_available_moves()
                    
                    degrees += 90
                    if degrees > 270:
                        degrees = 0 #resetting degrees to 0 when a full circle has been completed
                    self.set_direction(degrees)
                        
                else:
                    print("dead end!, retracing steps!")
                    degrees += 180
                    if degrees > 270:
                        degrees = 0 #resetting degrees to 0 when a full circle has been completed
                    self.set_direction(degrees)
                                   