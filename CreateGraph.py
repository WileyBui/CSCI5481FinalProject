from eulerian_path import *

def reads_to_kmers(reads,k):
    kmers_dict = {}
    for r in reads:
        for i in range(len(r)-k+1):
            kmer = r[i:i+k]
            if kmer not in kmers_dict:
                kmers_dict[kmer] = 1
            else:
                kmers_dict[kmer] += 1
    return kmers_dict

def cleanup_kmers(kmers_dict):
    cleaned_kmers_dict = {}
    for kmer in kmers_dict:
        if kmers_dict[kmer] > 1:
            cleaned_kmers_dict[kmer] = kmers_dict[kmer]
    return cleaned_kmers_dict

def add_nodes_and_edges(kmers_list):
    graph = {}
    for kmer in kmers_list:
        left = kmer[:-1]
        right = kmer[1:]
        if left in graph:
            graph[left] += [right]
        else:
            graph[left] = [right]
    return graph

def dict_to_list(kmers_dict):
    list = []
    for kmer in kmers_dict:
        list += [kmer]*kmers_dict[kmer]
    return list

def de_bruijn(reads,k):
    kmers_dict = cleanup_kmers((reads_to_kmers(reads,k)))
    kmers_list = dict_to_list(kmers_dict)
    return add_nodes_and_edges(kmers_list)

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
    filenames = ["data_1.txt", "data_2.txt"]
    data_dict = {}
    
    for filename in filenames:
        data_dict[filename] = read_data(filename)
        
    for k in range(25, 36):
        for filename in filenames:
            sequences = data_dict[filename]
            print("\n\n==============================================")
            
            print("Constructing De Bruijn Graph for k={}... ".format(k), end="")
            graph = de_bruijn(sequences, k)
            print("success.")
            
            if (len(graph) == 0):
                print("Unsuccess: de_bruijn() returns 0 nodes...")
                return
            
            is_valid_eulerian_path, edges_in, edges_out = has_eulerian_path_and_get_edges(graph)
            
            if (is_valid_eulerian_path):
                print(filename, "Eulerian path: SUCCESSFULLY FOUND!")
            else:
                print(filename, "Eulerian path: UNSUCCESS, but found a partial assembled genome path...")
                
            start_vertex = get_starting_node(graph, edges_in, edges_out)
            path_list = depth_first_traveral(graph, start_vertex, edges_out)
            path = parse_data(path_list)
        
            save_results_to_file("Solutions1/k=" + str(k) + "_" + filename, path, is_valid_eulerian_path)

if __name__ == '__main__':
    main()