from graph import Graph

if __name__ == '__main__':
  perfect = Graph()
  for i in range(1, 101):
    perfect.add_node(i)
    
perfect.create_graph('Perfect')

perfect.maze_getter()

perfect.edges_getter()

perfect.get_node_walls()





