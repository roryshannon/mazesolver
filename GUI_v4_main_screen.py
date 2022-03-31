from tkinter import Frame, Button, Label, Tk, Canvas


class start_screen:
  def __init__(self):
     
    self.root = Tk()
    self.start_Main = Frame(self.root)
    self.start_Main.grid()
    
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
    maze_frame = Frame(main_frame,padx=100)
    maze_frame.grid(row=0,column=0)

    #maze frame
    #canvas widget? drawing commands
    canvas = Canvas(maze_frame)
    canvas.grid(row=0,column=1)
    canvas.create_line(10, 10, 10, 250, 250, 250, 250, 10, 10, 10)
    #canvas.create_line(20,20,21,20)
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
    canvas.create_line(82,106,82,154)
    canvas.create_line(202,106,202,130)

    canvas.create_line(58,106,58,154)
    
   
    
    
  
      

    #menu frame in th main frame
    #menu frame
    menu_frame= Frame(main_frame)
    menu_frame.grid(row=0,column=1)

    menu_label = Label(menu_frame, text="MENU")
    reset_button = Button(menu_frame,text="Reset",bg="light blue")
    go_button = Button(menu_frame,text="Go",bg="light blue")
    solver_button = Button(menu_frame,text="Solver Type",bg="light blue")
    maze_button = Button(menu_frame,text="Maze Type",bg="light blue")
    back_button = Button(menu_frame, text="Back",command=self.back,bg="pink")

    solver_type=Label(menu_frame,text="SOLVER: Tremaux")
    maze_type=Label(menu_frame,text="MAZE: Braided")
    

    menu_label.grid(row=0,column=0)
    go_button.grid(row=1,column=0,ipadx=30)
    solver_button.grid(row=2,column=0,ipadx=3)
    maze_button.grid(row=3,column=0,ipadx=6)
    reset_button.grid(row=4,column=0,ipadx=21)
    back_button.grid(row=5,column=0,ipadx=23)
    solver_type.grid(row=6,column=0,pady=10)
    maze_type.grid(row=7,column=0,pady=10)
    
    

    

    main_frame.grid(row=1,column=0)

  def buttonX(self):
    self.root.destroy()

  def back(self):
    self.root.destroy()
    
    