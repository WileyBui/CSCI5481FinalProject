
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

    return (graph,weights)
