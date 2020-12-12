

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
    for kmer in kmers_dict:
        if kmers_dict[kmer] <= 2:
            del kmers_dict[kmer]


def De_Bruijn_Graph(shotgun_seqs,k):
    kmers_dict = find_kmers(shotgun_seqs,k)
    clean_kmers(kmers_dict)
    graph,weight = construct_DeBruijn_graph(kmers_dict)


def main():
    kmers_dict = ['ATCTAGAGTATTAGGTTTGAAAACCCTTGC', 'TACTGCCTCTTATATACATCTCCGAGCCCA', 'CGAGACGTAGAGGATTCTCGTATGCCAGCT', 'TCTGATTGCAAAACAAAGTTTCTAATCCAC', 'CTCCTCGTGCACACGAGACCGGAGCCTATC', 'TCGTCTGCCGTCTTCTGCTTGAAAAAAAAA', 'CCCAACTCTAAATCCTCTCCCCCTCCTATT', 'ATCTTCTCTTCATTTTTTATAAACATAACC', 'GTAGATACACAAACACCAGCTTCTGATCTT', 'GTTTCTTATACACATCTCCGAGTCCACGAG', 'ACGTAGAGGTATCTCGTATGCCGTCTTCTG', 'CTTGATAAAACAAACACTTTTTTTTTTTAC', 'TTACCGTTTACTTCTTTACCTCCTCTCTTC', 'CCCCACCTCCCTTTCCTTTGTTTCATATAC', 'CATTATCTACTGACTAATAGATTACAGACT', 'TTCTCTTATTCACCTCTCCGACCCCCCCCG', 'ATGCCAGATTACGTGCTAAGCACTATGTGT', 'ACATCTGCCACTTATACACATCTCCGAGCC', 'CACGAGACGTAGAGGAACACCGAATGCCGT', 'CTTCTGCCTGTAAAAACCACATGACATTCT', 'CAGCATCTTACCCACATATACACGCCCACG', 'CGCAGGACTCTACTCTTGTATTCCTTCTTC', 'TTCTTGTGATTTAAAAAAAAGATAAAGAGC', 'TAAACACTATGTGTACATTTTCTGTATGTT', 'CCTTTTGAAATTAAATTGGCAAAGAAATTT', 'GACCTGTCTCTTATACCACATCTCCGAGCC', 'CACGAGACGTAGAGGAATCTCGTATGCCGT', 'CTTCTGCTTGAAAAAAAAAAAACACATCAC', 'CTGCGCCTCCTTCTTCTCTCACCCCCCACG', 'GTGACCGTAGCGTCATCCCGCCGTTTTCCT', 'CGTCGCCGCATCCCCCCCATCCCACTCTGT', 'CTCTTCTCGCCCTCACCGCGCCCCCGCCAC', 'GCTACAGGAGCAGCAGGTAGGGGCGGGCCT', 'TGCTCTTATTCACAACTCTCTGACCACGAG', 'GCGTTGGGGAATCTTATACACCGCCCTTAG', 'CCCGCAAAAACAAAGCTTATCTCATCTGCC', 'GTCTTCTGCTTCTACAATATGTCTCTTATC', 'CACCTCTCCGAGCCCCCGAGACGCTCATGA', 'ATCTCCTCTTCCGTCTTCTGCTTGAACAAC', 'ACCGAAACCCCTCACCTTCCCCTACTTCCT', 'TTTTCAAACACGTGCAGGCTGTTTAATCTG', 'TCTCTTATACACATTCTCCGAGCCCACGAG', 'ACGTAGAGGAATCTCGTATGCCGTCTTCTG', 'CTTGAAAAAAACTAATATACACATCTCCGA', 'GCTCACGAGACAAGCAGCCATTTCGCATGC', 'AGACTTCTCCTTGAAAGAAAAAAAATCAAA', 'CTGCAACTCTATTTGTTTGAGTGTTACCAC']
    graph,weights = construct_DeBruijn_graph(kmers_dict)

    fake = ["abc","bca","cab","aba","aab"]
    graph,weights = construct_DeBruijn_graph(fake)
    print(graph)
    print(weights)
    for key in graph:
        print(len(graph[key]))


if __name__ == '__main__':
    main()
