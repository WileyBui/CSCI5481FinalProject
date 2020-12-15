from eulerian_path import *

def initialize_graph():
  graph = {}
  for i in range(0,7): 
    graph[str(i)] = []
  return graph


# TEST PART 1 => ['0', '1', '2', '0']
def test_1():
  graph = initialize_graph()
  graph["0"].append("1")
  graph["1"].append("2")
  graph["2"].append("0")
  is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
  start_vertex = get_starting_node(graph, edges_in, edges_out)
  path = depth_first_traveral(graph, start_vertex, edges_out)
  return is_valid_eulerian_path == True and path == ['0', '1', '2', '0']

# TEST PART 2 => ['0', '1', '3', '4', '1', '2', '0']
def test_2():
  graph = initialize_graph()
  graph["0"].append("1")
  graph["1"].append("3")
  graph["3"].append("4")
  graph["4"].append("1")
  graph["1"].append("2")
  graph["2"].append("0")
  is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
  start_vertex = get_starting_node(graph, edges_in, edges_out)
  path = depth_first_traveral(graph, start_vertex, edges_out)
  return is_valid_eulerian_path == True and path == ['0', '1', '3', '4', '1', '2', '0']

# TEST PART 3 => ['0', '6', '4', '5', '0', '1', '2', '3', '4', '2', '0']
def test_3():
  graph = initialize_graph()
  graph["0"].append("1")
  graph["0"].append("6")
  graph["1"].append("2")
  graph["2"].append("0")
  graph["2"].append("3")
  graph["3"].append("4")
  graph["4"].append("2")
  graph["4"].append("5")
  graph["5"].append("0")
  graph["6"].append("4")
  is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
  start_vertex = get_starting_node(graph, edges_in, edges_out)
  path = depth_first_traveral(graph, start_vertex, edges_out)
  return is_valid_eulerian_path == True and path == ['0', '6', '4', '5', '0', '1', '2', '3', '4', '2', '0']


# TEST PART 4 => ['1', '3', '1', '2', '4', '6', '3', '2', '2', '4', '3', '5', '6']
def test_4():
  graph = initialize_graph()
  graph["0"].append("0")
  graph["1"].append("2")
  graph["1"].append("3")
  graph["2"].append("2")
  graph["2"].append("4")
  graph["2"].append("4")
  graph["4"].append("3")
  graph["4"].append("6")
  graph["6"].append("3")
  graph["3"].append("2")
  graph["3"].append("5")
  graph["3"].append("1")
  graph["5"].append("6")
  is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
  start_vertex = get_starting_node(graph, edges_in, edges_out)
  path = depth_first_traveral(graph, start_vertex, edges_out)
  return is_valid_eulerian_path == True and path == ['1', '3', '1', '2', '4', '6', '3', '2', '2', '4', '3', '5', '6']

# TEST PART 5
def test_5():
  graph = initialize_graph()
  graph["1"].append("0")
  graph["0"].append("2")
  graph["2"].append("1")
  graph["0"].append("3")
  graph["3"].append("4")
  is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
  start_vertex = get_starting_node(graph, edges_in, edges_out)
  path = depth_first_traveral(graph, start_vertex, edges_out)
  return is_valid_eulerian_path == True and path == ['0', '2', '1', '0', '3', '4']


# TEST PART 6
def test_6():
  graph = initialize_graph()
  graph["1"].append("0")
  graph["0"].append("2")
  graph["2"].append("1")
  graph["0"].append("3")
  graph["3"].append("4")
  graph["4"].append("0")

  is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
  start_vertex = get_starting_node(graph, edges_in, edges_out)
  path = depth_first_traveral(graph, start_vertex, edges_out)
  return is_valid_eulerian_path == True and path == ['0', '3', '4', '0', '2', '1', '0']

# TEST PART 7
def test_7():
  graph = initialize_graph()
  graph["1"].append("0")
  graph["0"].append("2")
  graph["2"].append("1")
  graph["0"].append("3")
  graph["3"].append("4")
  graph["1"].append("3")
  is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
  start_vertex = get_starting_node(graph, edges_in, edges_out)
  return is_valid_eulerian_path == False


print("Test 1 passed:", bool(test_1))
print("Test 2 passed:", bool(test_2))
print("Test 3 passed:", bool(test_3))
print("Test 4 passed:", bool(test_4))
print("Test 5 passed:", bool(test_5))
print("Test 6 passed:", bool(test_6))
print("Test 7 passed:", bool(test_7))