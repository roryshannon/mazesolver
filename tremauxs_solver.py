import time

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
            self.conpass = "South"
            
            
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
        
    def make_move(self):
        degrees = 0
        
        while self.current_square != self.end_square: #until we are at the end
            
            '''if len(self.connections) > 2:
                print("at a junction! we must decide what to do!")
                print(f"these are the possible connections: {self.connections}, but we have just come from {self.current_square-self.forward}")'''
                
                
                
            if self.current_square + self.forward in self.connections:
                print("moving forward") #so the follower should go forward
                if len(self.connections) > 2: #this runs if the square is a junction, and then adds the chose path into the visited list
                    self.mark_as_visited()
                    print(self.visited)
                           
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
                print("moving left") #so the follower should turn left, as the wall has run out
                self.current_square = self.current_square + self.left
                self.connections = self.get_available_moves()
                
                degrees += 90
                if degrees > 270:
                    degrees = 0 #resetting degrees to 0 when a full circle has been completed
                self.set_direction(degrees)
                    
            else:
                print("dead end!, retracing steps!")
                #this is only important when we get back to the original junction!
                
                degrees += 180
                if degrees > 270:
                    degrees = 0 #resetting degrees to 0 when a full circle has been completed
                self.set_direction(degrees)
                                   