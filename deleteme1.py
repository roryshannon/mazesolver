def make_move(self):
        degrees = 0
        
        while self.current_square != self.end_square:
            
            
            if len(self.connections) > 2:
                print('juntion')
                #node = Node(self.current_square)
                
                #how to use recursion!!
                
                if self.current_square not in self.visited:
                    
                    #self.visited.append(self.current_square)
                    
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
                        
                        degrees += - 90
                        if degrees < 0:
                            degrees = 270 #circle for the degrees
                        self.set_direction(degrees) 
                    
                
                    elif self.current_square + self.left in self.connections:
                        print("moving left") 
                        self.current_square = self.current_square + self.left
                        self.visited.append(self.current_square)
                        
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
                    
                #DEAD END MOVE
                elif self.current_square in self.visited:
                    print("dead end!, retracing steps!")
                    time.sleep(0.2)
                    degrees += 180
                    if degrees > 270:
                        degrees = 0 #resetting degrees to 0 when a full circle has been completed
                    self.set_direction(degrees)
                    
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
                    
                
                
                    
                      
            #OG IF NO JUNCT
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