import time

class wall_follower:
    def __init__(self):
        self.name = "theseus" #a simple initial variable i decalred
        self.degrees = 0 # a way to have the wall follower facing the correct direction when starting
        direction_facing = "North" #a variable which was going to be used to read out the direction the wall follower was travelling but not needed due to the GUI
        
    def set_terminal_squares(self, start, end): #setter for the start and end square as they are different between my two mazes, and this adds compatability for other mazes
        self.start_square = start 
        self.end_square = end   
    
    def set_ROW(self, ROW): #sets the row, this also allows compatability for different size and shape mazes as this is what allows the maze solver to move up and down one square
        self.ROW = ROW    
    
    def set_direction(self, degrees): #this function resets the direction of the wall follower after a move is made, so that the solver can go forward and backwards even at when turned to face the left or right or down
        
        self.degrees = degrees #makes self.degrees the value which has been passed in
        if self.degrees == 0: #if facing up, left and right and one square to the side, whereas forward and back squares are the number of squares per row up and down
            self.forward = - self.ROW
            self.left = -1
            self.right = +1
            self.compass = "North"
            
            
        if self.degrees == 90: #similarly sets the values if the solver is facing left
            self.forward = -1
            self.left = + self.ROW
            self.right = - self.ROW
            self.compass = "West"
            
            
        if self.degrees == 180: #continues with the other possible directions
            self.forward = + self.ROW
            self.left = +1
            self.right = -1
            self.conpass = "South"
            
            
        if self.degrees == 270:
            self.forward = +1
            self.left = - self.ROW
            self.right = + self.ROW
            self.compass = "East"          
     
    def set_current_square(self, current): #allows the square the solver is in to change/update after it has made a move
        self.current_square = current
              
    def set_edges(self, edges): #allows the solver to update the squares it can move to from the new square, this is where all of the edges are defined, the "graph" is passed in from the main function to set all the edges as a dictionary
        self.edges = edges
        
    def get_available_moves(self): #this function is when the edges for the specific square the solver is on are found, and everytime the solver moves to a new square this is called again to get an updated list of the possible moves
        
        self.connections = self.edges[self.current_square]
        print(f"at {self.current_square} theseus can move to: {self.connections}")
        
        return self.connections
        
    def make_move(self): #this is the "meat" of the wall following algorithm, essentially it check using an if staement of the wall left would be a valid move, if not it checks the square ahead, if not it checks the square to the right, and if all of these are invalid we have reached a deadend and must turn around
        degrees = 0
        while self.current_square != self.end_square: #continues until the end square is found
            #time.sleep(0.2) ##initial tests to control speed
            
            if self.current_square + self.left in self.connections: #if the square to the left is valid
                print("moving left") #print statements used for initial testing
                self.current_square = self.current_square + self.left #move left / setting our location to the square to the left
                self.connections = self.get_available_moves() #resetting the possible moves for the left square
                
                degrees += 90 #changing the degrees as we have "turned" left
                if degrees > 270:
                    degrees = 0 #resetting degrees to 0 when a full circle has been completed
                self.set_direction(degrees) #using this degrees value to call the function which will correct the movement               
                
            elif self.current_square + self.forward in self.connections: #else if forward is a vlaid move
                print("moving forward") 
                self.current_square = self.current_square + self.forward #does the same but no need to change direction
                self.connections = self.get_available_moves() 
                
            elif self.current_square + self.right in self.connections:
                print("moving right") 
                self.current_square = self.current_square + self.right
                self.connections = self.get_available_moves()
                
                degrees += - 90
                if degrees < 0:
                    degrees = 270 #circle for the degrees
                self.set_direction(degrees) 
                    
            else: # if none of these moves are valid, it is a deadend and so the solver sets the direction to turn around
                print("dead end!, retracing steps!")
                degrees += 180
                if degrees > 270:
                    degrees = 0 #resetting degrees to 0 when a full circle has been completed
                self.set_direction(degrees)
                