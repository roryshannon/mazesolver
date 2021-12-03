from graph import Graph

if __name__ == '__main__':
  perfect = Graph()
  for i in range(1, 101):
    perfect.add_node(i)
    
perfect.create_graph('Perfect')

perfect.get()

perfect.edges_getter()





