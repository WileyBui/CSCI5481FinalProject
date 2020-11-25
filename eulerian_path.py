# import networkx as nx  
# import matplotlib
# import matplotlib.pyplot as plt
    
def has_eulerian_path_and_get_edges(graph):
  """
  This has_eulerian_path_and_get_edges function checks to see if a given graph
  can be an eulerian path. It checks to see if every node in the graph has at 
  most (outgoing edges - incoming edges) = 1 edge and at most 
  (incoming edges - outgoing edges) = 1 edge while all other nodes have equal
  incoming and outgoing edges.
  
  Returns (if there is an eulerian_path, incoming edges, and outgoing edges dictionary)
  """
  edges_in   = {}  # incoming edges
  edges_out  = {}  # outgoing edges
  
  # initialize incoming & outgoing edges with 0
  for vertex in graph.keys():
    edges_in[vertex]  = 0
    edges_out[vertex] = 0
   
  # updates on where the edge is coming from and to (edges_out/edges_in)
  for current_node in graph:
    for out_going_edge in graph[current_node]:
      edges_out[current_node] += 1
      edges_in[out_going_edge] += 1
      
  
  extra_node_in   = 0
  extra_node_out  = 0
  
  for i in graph:
    # has more than 1 extra edge in node results no eulerian path
    if (abs(edges_out[i] - edges_in[i]) > 1):
      return False, {}, {}
    
    # If there's an extra edge coming in or coming out from 1 node to another,
    # we add it up. It means that the extra edge that's coming out is the starting 
    # point and the extra edge that's coming in is the end point. However, we cannot
    # have multiple extra edges. Only 1 max.
    if (edges_in[i] - edges_out[i] == 1):
      extra_node_in += 1
    elif (edges_out[i] - edges_in[i] == 1):
      extra_node_out += 1
      
  return (extra_node_out == 0 and extra_node_in == 0) or (extra_node_out == 1 and extra_node_in == 1), edges_in, edges_out

def get_starting_node(graph, edges_in, edges_out):
  """
  If a vertex has an extra outgoing edge, then it's a start node.
  Otherwise, we can pick any vertex as a start node, so we picked
  the first key in the graph instead.
  """
  graph_length = len(graph)
  
  for vertex in graph:
    if (edges_out[vertex] - edges_in[vertex] == 1):
      return vertex
  return list(graph.keys())[0]

def depth_first_traveral(graph, start_node, edges_out):
  """
    We begin with a start node and traverse through the graph by following the edges
    from that starting node. Then we use an edge from that starting node to 
    traverse/visit through its edges by recursion until there are no edges left in a node.
    This doesn't mean all edges are discovered, so we use backtracking to discover
    the remaining unvisited edges until all edges are found. When there is no outgoing
    edge left in a node, we pre-append that node to the path.
  
  Idea from:
    https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
    https://www.youtube.com/watch?v=8MpoO2zA2l
  """
  
  path = []
  def dfs(current_node):
    # print("current: {}; edges_out: {}".format(current_node, edges_out))
    
    # keeps traversing until all outgoing edges are equal to 0
    while (edges_out[current_node] != 0):
      edges_out[current_node] -= 1  # visited the node, so we remove 1 outgoing edge
      next_node = graph[current_node][edges_out[current_node]]  # to visit the next node
      dfs(next_node)
    path.insert(0, current_node)    # pre-append to the path when no outgoing edges are left
    
  dfs(start_node)
  print(path)
  return path

if __name__ == "__main__": 
  
    graph = {}
    for i in range(0,7): 
      graph[str(i)] = []
  
  
    # TEST PART 1 => ['0', '1', '2', '0']
    # graph["0"].append("1")
    # graph["1"].append("2")
    # graph["2"].append("0")
    # is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    # start_vertex = get_starting_node(graph, edges_in, edges_out)
    # path = depth_first_traveral(graph, start_vertex, edges_out)
    # assert is_valid_eulerian_path == True
    # assert path == ['0', '1', '2', '0']
    
    # TEST PART 2 => ['0', '1', '3', '4', '1', '2', '0']
    # graph["0"].append("1")
    # graph["1"].append("3")
    # graph["3"].append("4")
    # graph["4"].append("1")
    # graph["1"].append("2")
    # graph["2"].append("0")
    # is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    # start_vertex = get_starting_node(graph, edges_in, edges_out)
    # path = depth_first_traveral(graph, start_vertex, edges_out)
    # assert is_valid_eulerian_path == True
    # assert path == ['0', '1', '3', '4', '1', '2', '0']
    
    # TEST PART 3 => ['0', '6', '4', '5', '0', '1', '2', '3', '4', '2', '0']
    # graph["0"].append("1")
    # graph["0"].append("6")
    # graph["1"].append("2")
    # graph["2"].append("0")
    # graph["2"].append("3")
    # graph["3"].append("4")
    # graph["4"].append("2")
    # graph["4"].append("5")
    # graph["5"].append("0")
    # graph["6"].append("4")
    # is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    # start_vertex = get_starting_node(graph, edges_in, edges_out)
    # path = depth_first_traveral(graph, start_vertex, edges_out)
    # assert is_valid_eulerian_path == True
    # assert path == ['0', '6', '4', '5', '0', '1', '2', '3', '4', '2', '0']
    
    
    # TEST PART 4 => ['1', '3', '1', '2', '4', '6', '3', '2', '2', '4', '3', '5', '6']
    # graph["0"].append("0")
    # graph["1"].append("2")
    # graph["1"].append("3")
    # graph["2"].append("2")
    # graph["2"].append("4")
    # graph["2"].append("4")
    # graph["4"].append("3")
    # graph["4"].append("6")
    # graph["6"].append("3")
    # graph["3"].append("2")
    # graph["3"].append("5")
    # graph["3"].append("1")
    # graph["5"].append("6")
    # is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    # start_vertex = get_starting_node(graph, edges_in, edges_out)
    # path = depth_first_traveral(graph, start_vertex, edges_out)
    # assert is_valid_eulerian_path == True
    # assert path == ['1', '3', '1', '2', '4', '6', '3', '2', '2', '4', '3', '5', '6']
    
    # TEST PART 5
    # graph["1"].append("0")
    # graph["0"].append("2")
    # graph["2"].append("1")
    # graph["0"].append("3")
    # graph["3"].append("4")
    # is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    # start_vertex = get_starting_node(graph, edges_in, edges_out)
    # path = depth_first_traveral(graph, start_vertex, edges_out)
    # assert is_valid_eulerian_path == True
    # assert path == ['0', '2', '1', '0', '3', '4']
    
    
    # TEST PART 6
    graph["1"].append("0")
    graph["0"].append("2")
    graph["2"].append("1")
    graph["0"].append("3")
    graph["3"].append("4")
    graph["4"].append("0")
    is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    start_vertex = get_starting_node(graph, edges_in, edges_out)
    path = depth_first_traveral(graph, start_vertex, edges_out)
    assert is_valid_eulerian_path == True
    assert path == ['0', '3', '4', '0', '2', '1', '0']
    
    # TEST PART 7
    # graph["1"].append("0")
    # graph["0"].append("2")
    # graph["2"].append("1")
    # graph["0"].append("3")
    # graph["3"].append("4")
    # graph["1"].append("3")
    # is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    # start_vertex = get_starting_node(graph, edges_in, edges_out)
    # assert is_valid_eulerian_path == False
    
    


    # is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
    
    # if (is_valid_eulerian_path):
    #   start_vertex = get_starting_node(graph, edges_in, edges_out)
    #   path = depth_first_traveral(graph, start_vertex, edges_out)
    #   assert path == ['1', '3', '1', '2', '4', '6', '3', '2', '2', '4', '3', '5', '6']
    # else:
    #   print("Error: eulerian path doesn't exist (probably has extra outgoing edges vs ingoing edges)")

    # fig = plt.figure(figsize=(12,12))
    # ax = plt.subplot(111)
    # ax.set_title('Graph - Shapes', fontsize=10)

    # G = nx.DiGraph()
    # G.add_node('shape1')
    # G.add_node('shape2')
    # G.add_node('shape3')
    # G.add_node('shape4')
    # G.add_edge('shape1', 'shape2')
    # G.add_edge('shape1', 'shape3')
    # G.add_edge('shape3', 'shape4')
    # pos = nx.spring_layout(G)
    # nx.draw(G, pos, node_size=1500, node_color='cyan', font_size=8, font_weight='bold')

    # plt.tight_layout()
    # plt.show()
    # plt.savefig("Graph1.png", format="PNG")
    
    
    
    """
    Extra edges that cannot be traversed -
      We use backtracking algorithm to traverse through every single edge.
      
      We begin with a start node and traverse through the graph by following the edges
      from that starting node. Then we use an edge from that starting node to 
      traverse/visit through its edges by recursion until there are no edges left in a node.
      This doesn't mean all edges are discovered, so we use backtracking to discover
      the remaining unvisited edges until all edges are found. When there is no outgoing
      edge left in a node, we pre-append that node to the path.
      
    Duplicate edges -
      As long as every node in the graph has at most (outgoing edges - incoming edges) = 1 edge
      and at most (incoming edges - outgoing edges) = 1 edge while all other nodes have equal
      incoming and outgoing edges. Then it can traverse through the duplicate edges.

    """