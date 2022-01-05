import time

class test():
    def __init__(self):
        self.current_square = 0
        self.forward = 1
        self.connections = []
        self.visited = []
        self.end = 3
        

    def deadend(self, degrees):
        degrees += 180 # run the deadend code
        if degrees > 270: #make it circular
            degrees = 0
                
        return degrees
    
    #gotta do 2 things for  a move: make the square the next square and reset the connections


    def testing_move(self):
        
        degrees = 0
        while self.current_square != self.end_square:
            
            if len(self.connections) > 2:
                for i in range(self.connections):
                    if self.connections[i] not in self.visited:
                        self.current_square = self.connections[i]
                        #how to make the move! call the below with a function?
                        
                        self.visited.append(self.current_square)
                        
                        
                        print(self.visited, self.current_square)
                        time.sleep(10000)
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
                        
                        
'''degrees = 0
        
        while self.current_square != self.end_square:
                
                
            if self.current_square + self.forward in self.connections:
                self.current_square = self.current_square + self.forward 
                
                move = self.crossed(self.connections) 
                if move == True:
                    #degrees = self.deadend(degrees)
                    pass       
                else:
                    self.mark_as_visited()
                    self.connections = self.get_available_moves()
                           

                
            elif self.current_square + self.right in self.connections:
                self.current_square = self.current_square + self.right
                
                move = self.crossed(self.connections) 
                if move == True:
                    degrees = self.deadend()       
                else:
                    self.mark_as_visited()
                    self.connections = self.get_available_moves()
                    degrees += - 90
                    if degrees < 0:
                        degrees = 270 
                    self.set_direction(degrees)
                
            elif self.current_square + self.left in self.connections:
                self.current_square = self.current_square + self.right
                
                move = self.crossed(self.connections) 
                if move == True:
                    degrees = self.deadend(degrees)       
                else:
                    self.mark_as_visited()
                    self.connections = self.get_available_moves()
                    degrees += 90
                    if degrees > 270:
                        degrees = 0 
                    self.set_direction(degrees)
                
                
                
                    
            else:
                print("deadend")
                degrees = self.deadend(degrees)'''