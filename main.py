from graph import Graph
from wall_follower import wall_follower
from tremauxs_solver import Tremauxs

if __name__ == '__main__':
  perfect = Graph()
  for i in range(1, 101):
    perfect.add_node(i)
 
 
perfect.create_graph('Braided')

perfect.maze_getter()

#perfect.get_node_walls() 
 
    
def wall_follower_function():
  
  solve = wall_follower()
  solve.set_terminal_squares(perfect.start_getter(), perfect.end_getter())
  solve.set_ROW(perfect.ROW_getter())
  solve.set_direction(0)
  solve.set_current_square(perfect.start_getter())
  solve.set_edges(perfect.edges_getter())
  solve.get_available_moves()
  solve.make_move()    
    

def tremaux_solver_function():
  tremauxs = Tremauxs()
  tremauxs.set_terminal_squares(perfect.start_getter(), perfect.end_getter())
  tremauxs.set_ROW(perfect.ROW_getter())
  tremauxs.set_direction()
  tremauxs.set_current_square(perfect.start_getter())
  tremauxs.set_edges(perfect.edges_getter())
  tremauxs.get_available_moves()
  tremauxs.go() 
    

wall_follower_function()
#tremaux_solver_function()