from tkinter import Frame, Button, Label, Tk, Canvas
from graph import Graph
import time
from termios import NOFLSH
import sys
from node import Node

class start_screen:
  def __init__(self):
     
    self.root = Tk()
    self.start_Main = Frame(self.root)
    self.start_Main.grid()
    self.Boo = True
    self.BooS = True
    
    top_frame = Frame(self.start_Main,bg="light grey",pady=1)
    #in top frame
    myButton1 = Button(top_frame, text="X",bg='red',command=self.buttonX)
    myLabel2 = Label(top_frame, text="Rorys Maze Solver")
    #grid top
    top_frame.grid(row=0,column=0)
    myButton1.grid(row=0,column=3)
    myLabel2.grid(row=0,column=0,padx=270,pady=5)

    main_frame=Frame(self.start_Main)
    #maze frame in main frame
    self.maze_frame = Frame(main_frame,padx=100)
    self.maze_frame.grid(row=0,column=0)

    self.perfect_frame = Frame(self.maze_frame)
    self.perfect_frame.grid(row=0,column=0)

    #maze frame
    #canvas widget
    
    canvas = Canvas(self.perfect_frame)
    canvas.grid(row=0,column=1)
    #making the outline / square
    canvas.create_line(10, 10, 10, 250, 250, 250, 250, 10, 10, 10) 
    canvas.create_line(226,10,226,34)
    
    canvas.create_line(34,34,58,34)
    canvas.create_line(82,34,106,34)
    canvas.create_line(130,34,178,34)

    canvas.create_line(34,34,34,58)
    canvas.create_line(106,34,106,58)
    canvas.create_line(154,34,154,82)
    canvas.create_line(202,34,202,58)

    canvas.create_line(34,58,130,58)
    canvas.create_line(154,58,202,58)

    canvas.create_line(130,58,130,130)
    canvas.create_line(226,58,226,130)

    canvas.create_line(58,82,106,82)
    canvas.create_line(130,82,154,82)
    canvas.create_line(178,82,202,82)

    canvas.create_line(34,82,34,106)
    canvas.create_line(106,82,106,106)
    canvas.create_line(178,82,178,106)

    canvas.create_line(34,106,58,106)
    canvas.create_line(82,106,106,106)
    canvas.create_line(154,106,202,106)

    canvas.create_line(58,106,58,154)
    canvas.create_line(82,106,82,202)
    canvas.create_line(202,106,202,130)

    canvas.create_line(10,130,34,130)
    canvas.create_line(106,130,130,130)
    canvas.create_line(154,130,250,130)

    canvas.create_line(34,130,34,178)
    canvas.create_line(106,130,106,178)
    canvas.create_line(178,130,178,154)

    canvas.create_line(58,154,82,154)
    canvas.create_line(130,154,178,154)
    canvas.create_line(202,154,226,154)

    canvas.create_line(130,154,130,178)
    canvas.create_line(202,154,202,178)
    canvas.create_line(226,154,226,202)

    canvas.create_line(106,178,130,178)
    canvas.create_line(154,178,202,178)

    canvas.create_line(58,178,58,250)
    canvas.create_line(154,178,154,202)

    canvas.create_line(10,202,34,202)
    canvas.create_line(82,202,154,202)
    canvas.create_line(202,202,226,202)

    canvas.create_line(178,202,178,226)
    canvas.create_line(202,202,202,250)

    canvas.create_line(34,226,82,226)
    canvas.create_line(106,226,178,226)
    canvas.create_line(226,226,250,226)

    canvas.create_line(130,226,130,250)
    canvas.create_oval(15, 15, 30, 30,fill="green")

    #menu frame in th main frame
    #menu frame
    self.menu_frame= Frame(main_frame)
    self.menu_frame.grid(row=0,column=1)

    menu_label = Label(self.menu_frame, text="MENU")
    reset_button = Button(self.menu_frame,text="Reset",bg="light blue")
    go_button = Button(self.menu_frame,text="Go",bg="light blue",command=self.go)
    solver_button = Button(self.menu_frame,text="Solver Type",bg="light blue",command=self.solver_type)
    maze_button = Button(self.menu_frame,text="Maze Type",bg="light blue",command=self.maze_type)
    back_button = Button(self.menu_frame, text="Back",command=self.back,bg="pink")

    self.solver_type=Label(self.menu_frame,text="SOLVER: Wall Follower")
    self.maze_type=Label(self.menu_frame,text="MAZE: Perfect")
    

    menu_label.grid(row=0,column=0)
    go_button.grid(row=1,column=0,ipadx=30)
    solver_button.grid(row=2,column=0,ipadx=3)
    maze_button.grid(row=3,column=0,ipadx=6)
    reset_button.grid(row=4,column=0,ipadx=21)
    back_button.grid(row=5,column=0,ipadx=23)
    self.solver_type.grid(row=6,column=0,pady=10)
    self.maze_type.grid(row=7,column=0,pady=10)
    
    

    

    main_frame.grid(row=1,column=0)

  def buttonX(self):
    self.root.destroy()

  def back(self):
    self.root.destroy()

  def solver_type(self):
    if self.BooS == True:
      self.BooS = False
      self.solver_type.destroy()
      self.solver_type=Label(self.menu_frame,text="SOLVER: Tremaux")
      self.solver_type.grid(row=6,column=0,pady=10)
      
    else:
      self.BooS = True
      self.solver_type.destroy()
      self.solver_type=Label(self.menu_frame,text="SOLVER: Wall Follower")
      self.solver_type.grid(row=6,column=0,pady=10)
        


  def go(self):
    perfect = Graph()
    for i in range(1, 101):
      perfect.add_node(i)
     
    perfect.create_graph(self.maze_type_arg)
    
    
    #perfect.get_node_walls()   
        
    
    def tremaux_solver_function():
      tremauxs = Tremauxs()
      tremauxs.set_terminal_squares(perfect.start_getter(), perfect.end_getter())
      tremauxs.set_ROW(perfect.ROW_getter())
      tremauxs.set_direction()
      tremauxs.set_current_square(perfect.start_getter())
      tremauxs.set_edges(perfect.edges_getter())
      tremauxs.get_available_moves()
      tremauxs.go() 
        
    
    #wall_follower_function()
    #tremaux_solver_function()

    
  def maze_type(self):
    
    if self.Boo == False:
      self.Boo = True
      self.maze_type.destroy()
      self.maze_type=Label(self.menu_frame,text="MAZE: Perfect")
      self.maze_type.grid(row=7,column=0,pady=10)

      self.perfect_frame.destroy()
    
      self.perfect_frame = Frame(self.maze_frame)
      self.perfect_frame.grid(row=0,column=0)
      
      self.maze_type_arg = "Perfect"
      print(self.maze_type_arg)
      
      canvas = Canvas(self.perfect_frame)
      canvas.grid(row=0,column=1)
      #making the outline / square
      canvas.create_line(10, 10, 10, 250, 250, 250, 250, 10, 10, 10)

      ## 
      #making the perfect maze
      canvas.create_line(226,10,226,34)
    
      canvas.create_line(34,34,58,34)
      canvas.create_line(82,34,106,34)
      canvas.create_line(130,34,178,34)
  
      canvas.create_line(34,34,34,58)
      canvas.create_line(106,34,106,58)
      canvas.create_line(154,34,154,82)
      canvas.create_line(202,34,202,58)
  
      canvas.create_line(34,58,130,58)
      canvas.create_line(154,58,202,58)
  
      canvas.create_line(130,58,130,130)
      canvas.create_line(226,58,226,130)
  
      canvas.create_line(58,82,106,82)
      canvas.create_line(130,82,154,82)
      canvas.create_line(178,82,202,82)
  
      canvas.create_line(34,82,34,106)
      canvas.create_line(106,82,106,106)
      canvas.create_line(178,82,178,106)
  
      canvas.create_line(34,106,58,106)
      canvas.create_line(82,106,106,106)
      canvas.create_line(154,106,202,106)
  
      canvas.create_line(58,106,58,154)
      canvas.create_line(82,106,82,202)
      canvas.create_line(202,106,202,130)
  
      canvas.create_line(10,130,34,130)
      canvas.create_line(106,130,130,130)
      canvas.create_line(154,130,250,130)
  
      canvas.create_line(34,130,34,178)
      canvas.create_line(106,130,106,178)
      canvas.create_line(178,130,178,154)
  
      canvas.create_line(58,154,82,154)
      canvas.create_line(130,154,178,154)
      canvas.create_line(202,154,226,154)
  
      canvas.create_line(130,154,130,178)
      canvas.create_line(202,154,202,178)
      canvas.create_line(226,154,226,202)
  
      canvas.create_line(106,178,130,178)
      canvas.create_line(154,178,202,178)
  
      canvas.create_line(58,178,58,250)
      canvas.create_line(154,178,154,202)
  
      canvas.create_line(10,202,34,202)
      canvas.create_line(82,202,154,202)
      canvas.create_line(202,202,226,202)
  
      canvas.create_line(178,202,178,226)
      canvas.create_line(202,202,202,250)
  
      canvas.create_line(34,226,82,226)
      canvas.create_line(106,226,178,226)
      canvas.create_line(226,226,250,226)
  
      canvas.create_line(130,226,130,250)
      ##

    else:
      self.Boo = False
      self.perfect_frame.destroy()
      self.maze_type.destroy()
      self.maze_type=Label(self.menu_frame,text="MAZE: Braided")
      self.maze_type.grid(row=7,column=0,pady=10)

      self.perfect_frame = Frame(self.maze_frame)
      self.perfect_frame.grid(row=0,column=0)

      self.maze_type_arg = "Braided"
      print(self.maze_type_arg)
      #print(self.maze_type)
      
      #maze frame
      #canvas widget
      
      canvas = Canvas(self.perfect_frame)
      canvas.grid(row=0,column=1)
      #making the outline / square
      canvas.create_line(10, 10, 10, 250, 250, 250, 250, 10, 10, 10)

      canvas.create_line(58,10,58,106)
      canvas.create_line(106,10,106,82)
      
      canvas.create_line(130,34,154,34)
      canvas.create_line(178,34,226,34)

      canvas.create_line(34,34,34,58)
      canvas.create_line(82,34,82,58)
      canvas.create_line(226,34,226,130)

      canvas.create_line(130,58,202,58)

      canvas.create_line(130,58,130,82)
      canvas.create_line(202,58,202,154)

      canvas.create_line(10,82,34,82)
      canvas.create_line(154,82,178,82)

      canvas.create_line(82,82,82,106)
      canvas.create_line(154,82,154,154)

      canvas.create_line(82,106,154,106)

      canvas.create_line(34,106,34,130)
      canvas.create_line(106,106,106,202)
      canvas.create_line(178,106,178,178)

      canvas.create_line(34,130,82,130)

      canvas.create_line(58,130,58,178)
      canvas.create_line(130,130,130,226)

      canvas.create_line(82,154,106,154)
      canvas.create_line(202,154,250,154)

      canvas.create_line(34,154,34,226)
      
      canvas.create_line(58,178,82,178)
      canvas.create_line(154,178,226,178)

      canvas.create_line(154,178,154,226)
      canvas.create_line(202,178,202,226)

      canvas.create_line(34,202,82,202)

      canvas.create_line(178,202,178,250)
      canvas.create_line(226,202,226,226)

      canvas.create_line(82,226,130,226)

      canvas.create_line(58,226,58,250)
      
  def wall(self):
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
          #time.sleep(0.2) #to control speed!
          
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

  def wall_follower_function(self):
      
      self.set_terminal_squares(perfect.start_getter(), perfect.end_getter())
      set_ROW(perfect.ROW_getter())
      set_direction(0)
      set_current_square(perfect.start_getter())
      set_edges(perfect.edges_getter())
      get_available_moves()
      make_move() 
  

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