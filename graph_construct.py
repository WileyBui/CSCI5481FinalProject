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
        list += [kmer]
    return list

def de_bruijn(reads,k):
    kmers_dict = cleanup_kmers((reads_to_kmers(reads,k)))
    kmers_list = dict_to_list(kmers_dict)
    return add_nodes_and_edges(kmers_list)


def main():
    reads = ["AABBABAABB", "AAABB"]
    print(de_bruijn(reads, 2))

if __name__ == '__main__':
    main()