class wall_follower:
    def __init__(self):
        self.name = "theseus"
        self.degrees = 0
        direction_facing = "North"
        
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
        print(f"at {self.current_square} theseus can move to: {self.connections}")
        
        return self.connections
        
    def make_move(self):
        degrees = 0
        while self.current_square != self.end_square:
            if self.current_square + self.left in self.connections:
                print("moving left") #so the follower should turn left, as the wall has run out
                self.current_square = self.current_square + self.left
                self.connections = self.get_available_moves()
                degrees += 90
                if degrees > 270:
                    degrees = 0 #resetting degrees to 0 when a full circle has been completed
                self.set_direction(degrees)               
                
            elif self.current_square + self.forward in self.connections:
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
                    
            else:
                print("dead end!, retracing steps!")
                degrees += 180
                if degrees > 270:
                    degrees = 0 #resetting degrees to 0 when a full circle has been completed
                self.set_direction(degrees)
                
                
                #hhahahah i was missing a connection ugh
                #getting stuck at 12 13 14 on the maze! prehapos something I did wrong at dead end or maybe right, this is importnant as the wall follower should follow the wall round 4 to 3 to 13 to 14 to 13 to 12 to 13 to 3 to 2 
        
        
        
    