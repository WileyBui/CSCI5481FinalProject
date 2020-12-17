from graph_construct import *

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
      if (current_node not in edges_out):
        edges_out[current_node] = 0
      if (out_going_edge not in edges_in):
        edges_in[out_going_edge] = 0
        
      edges_out[current_node] += 1
      edges_in[out_going_edge] += 1
      
  
  extra_node_in   = 0
  extra_node_out  = 0
  
  for i in graph:
    # has more than 1 extra edge in node results no eulerian path
    if (abs(edges_out[i] - edges_in[i]) > 1):
      return False, edges_in, edges_out
    
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
    https://www.youtube.com/watch?v=8MpoO2zA2l4
  """
  
  path = []
  def dfs(current_node):
    # print("current: {}; edges_out: {}".format(current_node, edges_out))
    
    # keeps traversing until all outgoing edges are equal to 0 (or when a node is unexplorable)
    while (current_node in edges_out and edges_out[current_node] != 0):
      edges_out[current_node] -= 1  # visited the node, so we remove 1 outgoing edge
      next_node = graph[current_node][edges_out[current_node]]  # to visit the next node
      dfs(next_node)
    path.insert(0, current_node)    # pre-append to the path when no outgoing edges are left
    
  dfs(start_node)
  return path

def read_data(filename):
    f     = open(filename, "r")
    lines = f.readlines()
    f.close()
    
    sequences = []
    
    for line in lines:
        sequences.append(line.strip())
    return sequences

def parse_data(data):
    string = ""
    last_genome = ""
    for each in data:
        if last_genome != each:
            string += each[0]
            last_genome = each
    string += data[len(data) - 1][1:]
    return string
    
def save_results_to_file(output_file, results, success):
    f_write = open(output_file, "w+")
    if success:
        f_write.write("Success\n")
    else:
        f_write.write("Unsuccess\n")
        
    f_write.write(results)
    f_write.close()
    print("Successfully saved data to", output_file)
    
def main():
    filenames = ["data/data_1.txt", "data/data_2.txt"]
    data_dict = {}
    
    for filename in filenames:
        data_dict[filename] = read_data(filename)
        
    for k in range(15, 43):
        for filename in filenames:
            sequences = data_dict[filename]
            print("\n\n==============================================")
            
            print("Constructing De Bruijn Graph for k={}... ".format(k), end="")
            graph, weights = De_Bruijn_Graph(sequences, k)
            print("success.")
            
            is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
            
            if (is_valid_eulerian_path):
                print(filename, "Eulerian path: SUCCESSFULLY FOUND!")
            else:
                print(filename, "Eulerian path: UNSUCCESS, but found a partial assembled genome path...")
                
            start_vertex = get_starting_node(graph, edges_in, edges_out)
            path_list = depth_first_traveral(graph, start_vertex, edges_out)
            path = parse_data(path_list)
        
            save_results_to_file("Results/results_k=" + str(k) + "_" + filename, path, is_valid_eulerian_path)

if __name__ == '__main__':
  main()

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