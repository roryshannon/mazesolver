from tkinter import Frame, Button, Label, Tk, Canvas
from graph import Graph
import time
import sys

class start_screen:
  def __init__(self):
     
    self.root = Tk()
    self.start_Main = Frame(self.root)
    self.start_Main.grid()
    self.Boo = True
    self.BooS = True
    self.maze_type_arg = "Perfect"
    
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
    
    self.canvas = Canvas(self.perfect_frame)
    self.canvas.grid(row=0,column=1)
    #making the outline / square
    self.canvas.create_line(10, 10, 10, 250, 250, 250, 250, 10, 10, 10) 
    self.canvas.create_line(226,10,226,34)
    
    self.canvas.create_line(34,34,58,34)
    self.canvas.create_line(82,34,106,34)
    self.canvas.create_line(130,34,178,34)

    self.canvas.create_line(34,34,34,58)
    self.canvas.create_line(106,34,106,58)
    self.canvas.create_line(154,34,154,82)
    self.canvas.create_line(202,34,202,58)

    self.canvas.create_line(34,58,130,58)
    self.canvas.create_line(154,58,202,58)

    self.canvas.create_line(130,58,130,130)
    self.canvas.create_line(226,58,226,130)

    self.canvas.create_line(58,82,106,82)
    self.canvas.create_line(130,82,154,82)
    self.canvas.create_line(178,82,202,82)

    self.canvas.create_line(34,82,34,106)
    self.canvas.create_line(106,82,106,106)
    self.canvas.create_line(178,82,178,106)

    self.canvas.create_line(34,106,58,106)
    self.canvas.create_line(82,106,106,106)
    self.canvas.create_line(154,106,202,106)

    self.canvas.create_line(58,106,58,154)
    self.canvas.create_line(82,106,82,202)
    self.canvas.create_line(202,106,202,130)

    self.canvas.create_line(10,130,34,130)
    self.canvas.create_line(106,130,130,130)
    self.canvas.create_line(154,130,250,130)

    self.canvas.create_line(34,130,34,178)
    self.canvas.create_line(106,130,106,178)
    self.canvas.create_line(178,130,178,154)

    self.canvas.create_line(58,154,82,154)
    self.canvas.create_line(130,154,178,154)
    self.canvas.create_line(202,154,226,154)

    self.canvas.create_line(130,154,130,178)
    self.canvas.create_line(202,154,202,178)
    self.canvas.create_line(226,154,226,202)

    self.canvas.create_line(106,178,130,178)
    self.canvas.create_line(154,178,202,178)

    self.canvas.create_line(58,178,58,250)
    self.canvas.create_line(154,178,154,202)

    self.canvas.create_line(10,202,34,202)
    self.canvas.create_line(82,202,154,202)
    self.canvas.create_line(202,202,226,202)

    self.canvas.create_line(178,202,178,226)
    self.canvas.create_line(202,202,202,250)

    self.canvas.create_line(34,226,82,226)
    self.canvas.create_line(106,226,178,226)
    self.canvas.create_line(226,226,250,226)

    self.canvas.create_line(130,226,130,250)

    #menu frame in the main frame
    #menu frame
    self.menu_frame= Frame(main_frame)
    self.menu_frame.grid(row=0,column=1)

    menu_label = Label(self.menu_frame, text="MENU")
    reset_button = Button(self.menu_frame,text="Reset",bg="light blue",command=self.reset)
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

  def reset(self):
    self.root.destroy()
    start_screen()
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
    self.perfect = Graph()
    for i in range(1, 101):
      self.perfect.add_node(i)
     
    self.perfect.create_graph(self.maze_type_arg)
    
    self.wall_follower_function()
    
    #perfect.get_node_walls()    

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
      
      self.canvas = Canvas(self.perfect_frame)
      self.canvas.grid(row=0,column=1)
      #making the outline / square
      self.canvas.create_line(10, 10, 10, 250, 250, 250, 250, 10, 10, 10)

      ## 
      #making the perfect maze
      self.canvas.create_line(226,10,226,34)
    
      self.canvas.create_line(34,34,58,34)
      self.canvas.create_line(82,34,106,34)
      self.canvas.create_line(130,34,178,34)
  
      self.canvas.create_line(34,34,34,58)
      self.canvas.create_line(106,34,106,58)
      self.canvas.create_line(154,34,154,82)
      self.canvas.create_line(202,34,202,58)
  
      self.canvas.create_line(34,58,130,58)
      self.canvas.create_line(154,58,202,58)
  
      self.canvas.create_line(130,58,130,130)
      self.canvas.create_line(226,58,226,130)
  
      self.canvas.create_line(58,82,106,82)
      self.canvas.create_line(130,82,154,82)
      self.canvas.create_line(178,82,202,82)
  
      self.canvas.create_line(34,82,34,106)
      self.canvas.create_line(106,82,106,106)
      self.canvas.create_line(178,82,178,106)
  
      self.canvas.create_line(34,106,58,106)
      self.canvas.create_line(82,106,106,106)
      self.canvas.create_line(154,106,202,106)
  
      self.canvas.create_line(58,106,58,154)
      self.canvas.create_line(82,106,82,202)
      self.canvas.create_line(202,106,202,130)
  
      self.canvas.create_line(10,130,34,130)
      self.canvas.create_line(106,130,130,130)
      self.canvas.create_line(154,130,250,130)
  
      self.canvas.create_line(34,130,34,178)
      self.canvas.create_line(106,130,106,178)
      self.canvas.create_line(178,130,178,154)
  
      self.canvas.create_line(58,154,82,154)
      self.canvas.create_line(130,154,178,154)
      self.canvas.create_line(202,154,226,154)
  
      self.canvas.create_line(130,154,130,178)
      self.canvas.create_line(202,154,202,178)
      self.canvas.create_line(226,154,226,202)
  
      self.canvas.create_line(106,178,130,178)
      self.canvas.create_line(154,178,202,178)
  
      self.canvas.create_line(58,178,58,250)
      self.canvas.create_line(154,178,154,202)
  
      self.canvas.create_line(10,202,34,202)
      self.canvas.create_line(82,202,154,202)
      self.canvas.create_line(202,202,226,202)
  
      self.canvas.create_line(178,202,178,226)
      self.canvas.create_line(202,202,202,250)
  
      self.canvas.create_line(34,226,82,226)
      self.canvas.create_line(106,226,178,226)
      self.canvas.create_line(226,226,250,226)
  
      self.canvas.create_line(130,226,130,250)
      self.canvas.create_rectangle(226, 106, 250, 130, fill='green', outline='green')
      self.canvas.create_rectangle(34, 226, 58, 250, fill='red', outline='red')
      
      
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
      
      self.canvas = Canvas(self.perfect_frame)
      self.canvas.grid(row=0,column=1)
      #making the outline / square
      self.canvas.create_line(10, 10, 10, 250, 250, 250, 250, 10, 10, 10)

      self.canvas.create_line(58,10,58,106)
      self.canvas.create_line(106,10,106,82)
      
      self.canvas.create_line(130,34,154,34)
      self.canvas.create_line(178,34,226,34)

      self.canvas.create_line(34,34,34,58)
      self.canvas.create_line(82,34,82,58)
      self.canvas.create_line(226,34,226,130)

      self.canvas.create_line(130,58,202,58)

      self.canvas.create_line(130,58,130,82)
      self.canvas.create_line(202,58,202,154)

      self.canvas.create_line(10,82,34,82)
      self.canvas.create_line(154,82,178,82)

      self.canvas.create_line(82,82,82,106)
      self.canvas.create_line(154,82,154,154)

      self.canvas.create_line(82,106,154,106)

      self.canvas.create_line(34,106,34,130)
      self.canvas.create_line(106,106,106,202)
      self.canvas.create_line(178,106,178,178)

      self.canvas.create_line(34,130,82,130)

      self.canvas.create_line(58,130,58,178)
      self.canvas.create_line(130,130,130,226)

      self.canvas.create_line(82,154,106,154)
      self.canvas.create_line(202,154,250,154)

      self.canvas.create_line(34,154,34,226)
      
      self.canvas.create_line(58,178,82,178)
      self.canvas.create_line(154,178,226,178)

      self.canvas.create_line(154,178,154,226)
      self.canvas.create_line(202,178,202,226)

      self.canvas.create_line(34,202,82,202)

      self.canvas.create_line(178,202,178,250)
      self.canvas.create_line(226,202,226,226)

      self.canvas.create_line(82,226,130,226)

      self.canvas.create_line(58,226,58,250)
      #75,91
      self.canvas.create_rectangle(106, 178, 130, 202, fill='green', outline='green')
      self.canvas.create_rectangle(10, 226, 34, 250, fill='red', outline='red')

  def add_to_screen(self):
      #vars for coords?
      
      print(self.current_square)
      if self.current_square == 1:
        self.canvas.create_oval(15,15,29,29,fill="green")
        self.canvas.update()
      elif self.current_square == 2:
        self.canvas.create_oval(39,15,53,29,fill="green")
        self.canvas.update()
      elif self.current_square == 3:
        self.canvas.create_oval(63,15,77,29,fill="green")
        self.canvas.update()
      elif self.current_square == 4:
        self.canvas.create_oval(87,15,101,29,fill="green")
        self.canvas.update()
      elif self.current_square == 5:
        self.canvas.create_oval(111,15,125,29,fill="green")
        self.canvas.update()
      elif self.current_square == 6:
        self.canvas.create_oval(135,15,149,29,fill="green")
        self.canvas.update()
      elif self.current_square == 7:
        self.canvas.create_oval(159,15,173,29,fill="green")
        self.canvas.update()
      elif self.current_square == 8:
        self.canvas.create_oval(183,15,197,29,fill="green")
        self.canvas.update()
      elif self.current_square == 9:
        self.canvas.create_oval(207,15,221,29,fill="green")
        self.canvas.update()
      elif self.current_square == 10:
        self.canvas.create_oval(231,15,245,29,fill="green")
        self.canvas.update()
      elif self.current_square == 11:
        self.canvas.create_oval(15,39,29,53,fill="green")
        self.canvas.update()
      elif self.current_square == 12:
        self.canvas.create_oval(39,39,53,53,fill="green")
        self.canvas.update()
      elif self.current_square == 13:
        self.canvas.create_oval(63,39,77,53,fill="green")
        self.canvas.update()
      elif self.current_square == 14:
        self.canvas.create_oval(87,39,101,53,fill="green")
        self.canvas.update()
      elif self.current_square == 15:
        self.canvas.create_oval(111,39,125,53,fill="green")
        self.canvas.update()
      elif self.current_square == 16:
        self.canvas.create_oval(135,39,149,53,fill="green")
        self.canvas.update()
      elif self.current_square == 17:
        self.canvas.create_oval(159,39,173,53,fill="green")
        self.canvas.update()
      elif self.current_square == 18:
        self.canvas.create_oval(183,39,197,53,fill="green")
        self.canvas.update()
      elif self.current_square == 19:
        self.canvas.create_oval(207,39,221,53,fill="green")
        self.canvas.update()
      elif self.current_square == 20:
        self.canvas.create_oval(231,39,245,53,fill="green")
        self.canvas.update()
      elif self.current_square == 21:
        self.canvas.create_oval(15,63,29,77,fill="green")
        self.canvas.update()
      elif self.current_square == 22:
        self.canvas.create_oval(39,63,53,77,fill="green")
        self.canvas.update()
      elif self.current_square == 23:
        self.canvas.create_oval(63,63,77,77,fill="green")
        self.canvas.update()
      elif self.current_square == 24:
        self.canvas.create_oval(87,63,101,77,fill="green")
        self.canvas.update()
      elif self.current_square == 25:
        self.canvas.create_oval(111,63,125,77,fill="green")
        self.canvas.update()
      elif self.current_square == 26:
        self.canvas.create_oval(135,63,149,77,fill="green")
        self.canvas.update()
      elif self.current_square == 27:
        self.canvas.create_oval(159,63,173,77,fill="green")
        self.canvas.update()
      elif self.current_square == 28:
        self.canvas.create_oval(183,63,197,77,fill="green")
        self.canvas.update()
      elif self.current_square == 29:
        self.canvas.create_oval(207,63,221,77,fill="green")
        self.canvas.update()
      elif self.current_square == 30:
        self.canvas.create_oval(231,63,245,77,fill="green")
        self.canvas.update()
      elif self.current_square == 31:
        self.canvas.create_oval(15,87,29,101,fill="green")
        self.canvas.update()
      elif self.current_square == 32:
        self.canvas.create_oval(39,87,53,101,fill="green")
        self.canvas.update()
      elif self.current_square == 33:
        self.canvas.create_oval(63,87,77,101,fill="green")
        self.canvas.update()
      elif self.current_square == 34:
        self.canvas.create_oval(87,87,101,101,fill="green")
        self.canvas.update()
      elif self.current_square == 35:
        self.canvas.create_oval(111,87,125,101,fill="green")
        self.canvas.update()
      elif self.current_square == 36:
        self.canvas.create_oval(135,87,149,101,fill="green")
        self.canvas.update()
      elif self.current_square == 37:
        self.canvas.create_oval(159,87,173,101,fill="green")
        self.canvas.update()
      elif self.current_square == 38:
        self.canvas.create_oval(183,87,197,101,fill="green")
        self.canvas.update()
      elif self.current_square == 39:
        self.canvas.create_oval(207,87,221,101,fill="green")
        self.canvas.update()
      elif self.current_square == 40:
        self.canvas.create_oval(231,87,245,101,fill="green")
        self.canvas.update()
      elif self.current_square == 41:
        self.canvas.create_oval(15,111,29,125,fill="green")
        self.canvas.update()
      elif self.current_square == 42:
        self.canvas.create_oval(39,111,53,125,fill="green")
        self.canvas.update()
      elif self.current_square == 43:
        self.canvas.create_oval(63,111,77,125,fill="green")
        self.canvas.update()
      elif self.current_square == 44:
        self.canvas.create_oval(87,111,101,125,fill="green")
        self.canvas.update()
      elif self.current_square == 45:
        self.canvas.create_oval(111,111,125,125,fill="green")
        self.canvas.update()
      elif self.current_square == 46:
        self.canvas.create_oval(135,111,149,125,fill="green")
        self.canvas.update()
      elif self.current_square == 47:
        self.canvas.create_oval(159,111,173,125,fill="green")
        self.canvas.update()
      elif self.current_square == 48:
        self.canvas.create_oval(183,111,197,125,fill="green")
        self.canvas.update()
      elif self.current_square == 49:
        self.canvas.create_oval(207,111,221,125,fill="green")
        self.canvas.update()
      elif self.current_square == 50:
        self.canvas.create_oval(231,111,245,125,fill="green")
        self.canvas.update()
      elif self.current_square == 51:
        self.canvas.create_oval(15,135,29,149,fill="green")
        self.canvas.update()
      elif self.current_square == 52:
        self.canvas.create_oval(39,135,53,149,fill="green")
        self.canvas.update()
      elif self.current_square == 53:
        self.canvas.create_oval(63,135,77,149,fill="green")
        self.canvas.update()
      elif self.current_square == 54:
        self.canvas.create_oval(87,135,101,149,fill="green")
        self.canvas.update()
      elif self.current_square == 55:
        self.canvas.create_oval(111,135,125,149,fill="green")
        self.canvas.update()
      elif self.current_square == 56:
        self.canvas.create_oval(135,135,149,149,fill="green")
        self.canvas.update()
      elif self.current_square == 57:
        self.canvas.create_oval(159,135,173,149,fill="green")
        self.canvas.update()
      elif self.current_square == 58:
        self.canvas.create_oval(183,135,197,149,fill="green")
        self.canvas.update()
      elif self.current_square == 59:
        self.canvas.create_oval(207,135,221,149,fill="green")
        self.canvas.update()
      elif self.current_square == 60:
        self.canvas.create_oval(231,135,245,149,fill="green")
        self.canvas.update()
      elif self.current_square == 61:
        self.canvas.create_oval(15,159,29,173,fill="green")
        self.canvas.update()
      elif self.current_square == 62:
        self.canvas.create_oval(39,159,53,173,fill="green")
        self.canvas.update()
      elif self.current_square == 63:
        self.canvas.create_oval(63,159,77,173,fill="green")
        self.canvas.update()
      elif self.current_square == 64:
        self.canvas.create_oval(87,159,101,173,fill="green")
        self.canvas.update()
      elif self.current_square == 65:
        self.canvas.create_oval(111,159,125,173,fill="green")
        self.canvas.update()
      elif self.current_square == 66:
        self.canvas.create_oval(135,159,149,173,fill="green")
        self.canvas.update()
      elif self.current_square == 67:
        self.canvas.create_oval(159,159,173,173,fill="green")
        self.canvas.update()
      elif self.current_square == 68:
        self.canvas.create_oval(183,159,197,173,fill="green")
        self.canvas.update()
      elif self.current_square == 69:
        self.canvas.create_oval(207,159,221,173,fill="green")
        self.canvas.update()
      elif self.current_square == 70:
        self.canvas.create_oval(231,159,245,173,fill="green")
        self.canvas.update()
      elif self.current_square == 71:
        self.canvas.create_oval(15,183,29,197,fill="green")
        self.canvas.update()
      elif self.current_square == 72:
        self.canvas.create_oval(39,183,53,197,fill="green")
        self.canvas.update()
      elif self.current_square == 73:
        self.canvas.create_oval(63,183,77,197,fill="green")
        self.canvas.update()
      elif self.current_square == 74:
        self.canvas.create_oval(87,183,101,197,fill="green")
        self.canvas.update()
      elif self.current_square == 75:
        self.canvas.create_oval(111,183,125,197,fill="green")
        self.canvas.update()
      elif self.current_square == 76:
        self.canvas.create_oval(135,183,149,197,fill="green")
        self.canvas.update()
      elif self.current_square == 77:
        self.canvas.create_oval(159,183,173,197,fill="green")
        self.canvas.update()
      elif self.current_square == 78:
        self.canvas.create_oval(183,183,197,197,fill="green")
        self.canvas.update()
      elif self.current_square == 79:
        self.canvas.create_oval(207,183,221,197,fill="green")
        self.canvas.update()
      elif self.current_square == 80:
        self.canvas.create_oval(231,183,245,197,fill="green")
        self.canvas.update()
      elif self.current_square == 81:
        self.canvas.create_oval(15,207,29,221,fill="green")
        self.canvas.update()
      elif self.current_square == 82:
        self.canvas.create_oval(39,207,53,221,fill="green")
        self.canvas.update()
      elif self.current_square == 83:
        self.canvas.create_oval(63,207,77,221,fill="green")
        self.canvas.update()
      elif self.current_square == 84:
        self.canvas.create_oval(87,207,101,221,fill="green")
        self.canvas.update()
      elif self.current_square == 85:
        self.canvas.create_oval(111,207,125,221,fill="green")
        self.canvas.update()
      elif self.current_square == 86:
        self.canvas.create_oval(135,207,149,221,fill="green")
        self.canvas.update()
      elif self.current_square == 87:
        self.canvas.create_oval(159,207,173,221,fill="green")
        self.canvas.update()
      elif self.current_square == 88:
        self.canvas.create_oval(183,207,197,221,fill="green")
        self.canvas.update()
      elif self.current_square == 89:
        self.canvas.create_oval(207,207,221,221,fill="green")
        self.canvas.update()
      elif self.current_square == 90:
        self.canvas.create_oval(231,207,245,221,fill="green")
        self.canvas.update()
      elif self.current_square == 91:
        self.canvas.create_oval(15,231,29,245,fill="green")
        self.canvas.update()
      elif self.current_square == 92:
        self.canvas.create_oval(39,231,53,245,fill="green")
        self.canvas.update()
      elif self.current_square == 93:
        self.canvas.create_oval(63,231,77,245,fill="green")
        self.canvas.update()
      elif self.current_square == 94:
        self.canvas.create_oval(87,231,101,245,fill="green")
        self.canvas.update()
      elif self.current_square == 95:
        self.canvas.create_oval(111,231,125,245,fill="green")
        self.canvas.update()
      elif self.current_square == 96:
        self.canvas.create_oval(135,231,149,245,fill="green")
        self.canvas.update()
      elif self.current_square == 97:
        self.canvas.create_oval(159,231,173,245,fill="green")
        self.canvas.update()
      elif self.current_square == 98:
        self.canvas.create_oval(183,231,197,245,fill="green")
        self.canvas.update()
      elif self.current_square == 99:
        self.canvas.create_oval(207,231,221,245,fill="green")
        self.canvas.update()
      elif self.current_square == 100:
        self.canvas.create_oval(231,231,245,245,fill="green")
        self.canvas.update()
      
        
      
      time.sleep(0.3)
      
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
          self.add_to_screen()

  def wall_follower_function(self):
      
    self.set_terminal_squares(self.perfect.start_getter(), self.perfect.end_getter())
    self.set_ROW(self.perfect.ROW_getter())
    self.set_direction(0)
    self.set_current_square(self.perfect.start_getter())
    self.set_edges(self.perfect.edges_getter())
    self.get_available_moves()
    self.make_move() 
  

  def trem(self):
      self.name = "tremaux"
      self.visited = []
      self.explored = []
      self.degrees = 0
      self.stack = []                  
    
  def go_pro(self):
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
                
  def tremaux_solver_function(self):
      self.trem()
      self.set_terminal_squares(self.perfect.start_getter(), self.perfect.end_getter())
      self.set_ROW(self.perfect.ROW_getter())
      self.set_direction()
      self.set_current_square(self.perfect.start_getter())
      self.set_edges(self.perfect.edges_getter())
      self.get_available_moves()
      self.go()
