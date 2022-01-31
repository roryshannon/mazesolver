from tkinter import *


class GUI:
    def __init__(self, parent):
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello, World!"
        self.button1["background"] = "green"     
        self.button1.pack(fill = X)             # note the use of the fill attribute

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Off to join the circus!") 
        self.button2.configure(background="tan")               
        self.button2.pack(ipadx = 5, ipady = 10)

        self.button3 = Button(self.myContainer1)
        self.button3.configure(text="Join me?", background="cyan")  
        self.button3.pack(fill = X, padx = 20, pady = 5)

        self.button4 = Button(self.myContainer1, text="Goodbye!", background="red") 
        self.button4.pack(fill = X, padx = 20, pady = 5)


root = Tk()
root.title("Maze Solver")
myapp = GUI(root)
root.mainloop()