from tkinter import *

root = Tk()


def buttonX():
  root.destroy()

def start_button():
  print("start")
  

title_frame = Frame(root,bg="light grey")
main_frame=Frame(root)

myButton1 = Button(title_frame, text="X",bg='red',command=buttonX)
myLabel2 = Label(title_frame, text="Rorys Maze Solver")

title_frame.grid(row=0,column=0)
myButton1.grid(row=0,column=3)
myLabel2.grid(row=0,column=0,padx=100,pady=5)


welcome_label = Label(main_frame, text="MAZE SOLVER")
start_button = Button(main_frame, text="start", command=start_button)
info_button = Button(main_frame, text="info")
credits_button = Button(main_frame, text="credits")
quit_button = Button(main_frame, text="quit")

welcome_label.grid(row=0, column=0)
start_button.grid(row=1,column=0)
info_button.grid(row=2,column=0)
credits_button.grid(row=3,column=0)
quit_button.grid(row=4,column=0)

main_frame.grid(row=1,column=0,pady=100)


root.mainloop()
