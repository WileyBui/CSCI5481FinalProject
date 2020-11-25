from eulerian_path import *

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