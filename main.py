from graph import Graph
from wall_follower import wall_follower
from tremauxs_solver import Tremauxs


#the code from this class was actually copied into the "start_screen" class as the function for the comand when pressing the "go" button, a neat way of doing the exact same thing just in a different placve after a user input
if __name__ == '__main__': #starts the program from the main.py file
  perfect = Graph() #initialised graph from the imported class
  for i in range(1, 101): #and adds 100 nodes (python goes between the two nubers hence 101)
    perfect.add_node(i) # for each adds a node with the "add node" method and the number in the list is sent as the id which works well to get nodes 1-100
 
 
perfect.create_graph('Braided') #passing through the type of maze here as part of early testing, but was changed when on my GUI to be used defined by a button press

perfect.maze_getter() #calls the maze getter function to see the maaze output, again as part of my early testing
perfect.get_node_walls() #more early testing this calls the get walls functions to see which nodes have connections where, I did not end up using this due to time constraints so it justs says true for all but it could be an area to expand upon or a better solution to some aspects of my code
 
    
def wall_follower_function(): #a way to call the funcitons to get the wall follower properly set up, perhaps not the best placement for this but functional and not necessarily terrible
  
  solve = wall_follower() 
  solve.set_terminal_squares(perfect.start_getter(), perfect.end_getter())
  solve.set_ROW(perfect.ROW_getter())
  solve.set_direction(0)
  solve.set_current_square(perfect.start_getter())
  solve.set_edges(perfect.edges_getter())
  solve.get_available_moves()
  solve.make_move()    #finishes with this function which does the bulk of the processing using the other functions to reset values after moving
    

def tremaux_solver_function():
  tremauxs = Tremauxs()
  tremauxs.set_terminal_squares(perfect.start_getter(), perfect.end_getter())
  tremauxs.set_ROW(perfect.ROW_getter())
  tremauxs.set_direction()
  tremauxs.set_current_square(perfect.start_getter())
  tremauxs.set_edges(perfect.edges_getter())
  tremauxs.get_available_moves()
  tremauxs.go() #same as wall follwer effectively uses other functions to reset values
    

#wall_follower_function() # a way to chose which solver was used (by commenting out the one you didnt want), very useful during early testing but also of course changed to a button imput for the GUI
#tremaux_solver_function()