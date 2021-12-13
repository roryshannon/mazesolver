from graph import Graph
from wall_follower import wall_follower

if __name__ == '__main__':
  perfect = Graph()
  for i in range(1, 101):
    perfect.add_node(i)
 
 
perfect.create_graph('Perfect')

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
    

wall_follower_function()