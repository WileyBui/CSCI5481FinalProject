from eulerian_path import *

def construct_DeBruijn_graph(kmers_dict):
    graph = {}
    weights = {}
    for kmer in kmers_dict:
        k = len(kmer)
        first_kminus1mer = kmer[:k-1]
        second_kmius1mer = kmer[1:]
        if first_kminus1mer not in graph:
            graph[first_kminus1mer] = [second_kmius1mer]
        else:
            graph[first_kminus1mer] = graph[first_kminus1mer] + [second_kmius1mer]

        if first_kminus1mer+"_to_"+second_kmius1mer not in weights:
            weights[first_kminus1mer+"_to_"+second_kmius1mer] = 1
        else:
            weights[first_kminus1mer+"_to_"+second_kmius1mer] += 1

    return (graph,weights)

def find_kmers(shotgun_seqs,k):
    kmers_dict = {}
    for seq in shotgun_seqs:
        for i in range(len(seq)-k+1):
            kmer = seq[i:i+k]
            if kmer in kmers_dict:
                kmers_dict[kmer] += 1
            else:
                kmers_dict[kmer] = 1
    return kmers_dict

def clean_kmers(kmers_dict):
    for kmer in list(kmers_dict):
        if kmers_dict[kmer] <= 2:
            del kmers_dict[kmer]


def De_Bruijn_Graph(shotgun_seqs,k):
    kmers_dict = find_kmers(shotgun_seqs,k)
    clean_kmers(kmers_dict)
    (graph,weight) = construct_DeBruijn_graph(kmers_dict)
    return (graph,weight)

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
    for each in data:
        string += each[0]
    string += data[len(data) - 1][1:len(data)]
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
    filenames = ["data_1.txt", "data_2.txt"]
    
    
    for filename in filenames:
        k = 3
        sequences = read_data(filename)
        print("\n\n==============================================")
        
        graph, weights = De_Bruijn_Graph(sequences, k)
        
        is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
        
        if (is_valid_eulerian_path):
            print(filename, "Eulerian path: SUCCESSFULLY FOUND!")
        else:
            print(filename, "Eulerian path: UNSUCCESS, but found a partial assembled genome path...")
            
        start_vertex = get_starting_node(graph, edges_in, edges_out)
        path_list = depth_first_traveral(graph, start_vertex, edges_out)
        path = parse_data(path_list)
    
        save_results_to_file("results_" + str(k) + "k_" + filename, path, is_valid_eulerian_path)

if __name__ == '__main__':
    main()