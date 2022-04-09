from node import Node

class Graph:
  def __init__(self): #initialising the graph with two dictionaries for nodes and conecctions
    self.node_list = {}
    self.edges = {}
    
    
  def create_graph(self, graph): #a rather inneficient way of defining which nodes are connected to which, by defining by hand and drawing reference from the maze i created to wrok from
    if graph == 'Perfect':
      self.start = 50 # defining the start and end points for the maze
      self.end = 92
      self.ROW = 10
      self.edges = {
        1: [2,11],
        2: [1,3],
        3: [2,4,13],
        4: [3,5],
        5: [4,6,15],
        6: [5,7],
        7: [6,8],
        8: [7,9,18],
        9: [8,19],
        10: [20],
        11: [1,21],
        12: [13],
        13: [3, 12,14],
        14: [13],
        15: [5,16],
        16: [15,26],
        17: [18],
        18: [8,17],
        19: [9,20,29],
        20: [10,19,30],
        21: [11,22,31],
        22: [21,23,32],
        23: [22,24],
        24: [23,25],
        25: [24,35],
        26: [16],
        27: [28,37],
        28: [27,29],
        29: [19,28,39],
        30: [20,40],
        31: [21,41],
        32: [22,33],
        33: [32,34,43],
        34: [33],
        35: [25,45],
        36: [37,46],
        37: [27,36],
        38: [39],
        39: [29,38,49],
        40: [30,50],
        41: [31,42],
        42: [41,52],
        43: [33,53],
        44: [45,54],
        45: [35,44],
        46: [36,47,56],
        47: [46,48],
        48: [47],
        49: [39],
        50: [40],
        51: [61],
        52: [42,62],
        53: [43],
        54: [44,64],
        55: [56,65],
        56: [46,55,57],
        57: [56],
        58: [59,68],
        59: [58,60],
        60: [59,70],
        61: [51,71],
        62: [52,63,72],
        63: [62,73],
        64: [54,74],
        65: [55],
        66: [67,76],
        67: [66,68],
        68: [58,67],
        69: [79],
        70: [60,80],
        71: [61,72],
        72: [62,71,82],
        73: [63,83],
        74: [64,75],
        75: [74,76],
        76: [66,75],
        77: [78,87],
        78: [77,79,88],
        79: [69,78],
        80: [70,90],
        81: [82,91],
        82: [72,81],
        83: [73,84],
        84: [83,85,94],
        85: [84,86],
        86: [85,87],
        87: [77,86],
        88: [78,98],
        89: [90,99],
        90: [80,89],
        91: [81,92],
        92: [91],
        93: [94],
        94: [84,93,95],
        95: [94],
        96: [97],
        97: [96,98],
        98: [88,97],
        99: [89,100],
        100: [99]
        }
    else:
      self.start = 75
      self.end = 91
      self.ROW = 10
      self.edges = {
        1: [2,11],
        2: [1,12],
        3: [4,13],
        4: [3,14],
        5: [6,15],
        6: [5,7],
        7: [6,8,17],
        8: [7,9],
        9: [8,10],
        10: [9,20],
        11: [1,21],
        12: [2,22],
        13: [3,13],
        14: [4,24],
        15: [5,16,25],
        16: [15,17],
        17: [7,16,18],
        18: [17,19],
        19: [18,29],
        20: [10,30],
        21: [11,22],
        22: [12,21,32],
        23: [13,24,33],
        24: [14,23,34],
        25: [15,35],
        26: [27,36],
        27: [26,28],
        28: [27,38],
        29: [19,39],
        30: [20,40],
        31: [32,41],
        32: [22,31,42],
        33: [23,43],
        34: [24,35],
        35: [25,34,36],
        36: [26,35],
        37: [38,47],
        38: [28,37,48],
        39: [29,49],
        40: [30,50],
        41: [31,51],
        42: [32,43],
        43: [33,42,44],
        44: [43,54],
        45: [46,55],
        46: [45,56],
        47: [37,57],
        48: [38,58],
        49: [39,59],
        50: [40,60],
        51: [41,52,61],
        52: [51,62],
        53: [54,63],
        54: [44,53],
        55: [45,65],
        56: [46,66],
        57: [47,67],
        58: [48,68],
        59: [49,60],
        60: [50,59],
        61: [51,71],
        62: [52,72],
        63: [53,64],
        64: [63,74],
        65: [55,75],
        66: [56,67,76],
        67: [57,66],
        68: [58,69],
        69: [68,70],
        70: [69,80],
        71: [61,81],
        72: [62,73],
        73: [72,74],
        74: [64,73,84],
        75: [65,85],
        76: [66,86],
        77: [78,87],
        78: [77,88],
        79: [80,89],
        80: [70,79,80],
        81: [71,91],
        82: [83,92],
        83: [82,84,93],
        84: [74,83,85],
        85: [75,84],
        86: [76,96],
        87: [77,97],
        88: [78,98],
        89: [79,99],
        90: [80,100],
        91: [81,92],
        92: [82,91],
        93: [83,94],
        94: [93,95],
        95: [94,96],
        96: [86,95,97],
        97: [87,96,],
        98: [88,99],
        99: [89,98],
        100:[90,99],
        }


  def add_node(self,key): #calling the Node class and instantiating a new node obejct for each square
    new_node = Node(key)
    #new_node.get_walls()
    self.node_list[key] = new_node #adding the new node to the graph dictionary node_list
    
  def edges_getter(self): #a getter for the edges of the graph
    #for i in self.edges:
      #print("Node", i, "Conected to nodes: ", end="")
      #print(self.edges[i])
    return self.edges
      
      
  def maze_getter(self):  #a way for me to print the maze before I had crated my GUI (so now a little redundant but useful at the time)
    for i in self.node_list:
      print("|", i, "|", end ="")
      if i < 10:
        print(" ", end="")
      if i % 10 == 0:
        print("|\n")
      
  def get_node_walls(self): #a getter to see which nodes had walls where (/ where the wasnt connections to eventually sent to a GUI if needed)
    for i in self.node_list:
      self.node_list[i].get_walls()
      
  def ROW_getter(self): #another getter but this time used together when changing the size of the maze, used by the set direction function to check how many squares on move "up" is
    return self.ROW
  
  def start_getter(self): # to access the start square
    return self.start
  
  def end_getter(self): # to access the end square
    return self.end
