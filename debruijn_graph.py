def construct_DeBruijn_graph(kmers_dict):
  graph = {}
  weights = {}
  for kmer in kmers_dict:
    k = len(kmer)
    first_kminus1mer = kmer[:k-1]
    second_kmius1mer = kmer[1:]
    weights[first_kminus1mer+"_to_"+second_kmius1mer] += 1
    if first_kminus1mer not in graph:
      graph[first_kminus1mer] = [second_kmius1mer]
    else:
      graph[first_kminus1mer] = graph[first_kminus1mer] + [second_kmius1mer]

    if first_kminus1mer+"_to_"+second_kmius1mer not in weights:
      weights[first_kminus1mer+"_to_"+second_kmius1mer] = 1
    else:
      weights[first_kminus1mer+"_to_"+second_kmius1mer] += 1

  return (graph, weights)

def break_into_kmers(data, k):
  data_length = len(data) // k
  k_mer = []
  
  for i in range(1, data_length + 1):
    k_mer.append(data[(i - 1) * k : i * k])
  return k_mer

def read_data(filename, k):
  f     = open(filename, "r")
  lines = f.readlines()
  f.close()
  
  kmers = []
  line_count = 0
  for line in lines:
    line_count += 1
    
    if ((line_count - 2) % 4 == 0):
      kmers += break_into_kmers(line.strip(), k)
  return kmers
  
  
if __name__ == "__main__":
  kmers = read_data("trimmomatic_outputs/output_forward_unpaired.fq", 30)
  print(kmers)
  # graph, weights = construct_DeBruijn_graph(kmers)