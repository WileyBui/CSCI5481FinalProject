def break_into_kmers(data, k):
  data_length = len(data) // k
  k_mer = []
  
  for i in range(1, data_length + 1):
    k_mer.append(data[(i - 1) * k : i * k])
  return k_mer

def clean_up_data(filename, output_file):
  """
  clean_up_data function picks only the sequences and quality scores from the filename
  param, and puts the results to its output_file
  """
  f     = open(filename, "r")
  lines = f.readlines()
  f.close()

  f_write = open(output_file, "w+")
  line_count = 0
  
  remove_chars_after = None
  current_sequence = None
  # sequences_and_scores = {}
  for line in lines:
    line_count += 1

    # lines 2, 6, 10, 14, ... are the sequences
    # lines 4, 8, 12, 16, ... are the quality scores
    if (line_count % 2 == 0 and not line_count % 4 == 0):
      line = line.strip()
      current_sequence = line
      remove_chars_after = len(line)
    elif (line_count % 4 == 0):
      line = line.strip()[:remove_chars_after]
      # sequences_and_scores[current_sequence] = line
      
      if (len(current_sequence) != len(line)):
        print("sequence & quality score length doesn't match... see line "\
              "#{} and {}".format(str(line_count-2), str(line_count)))
      else:
        f_write.write(current_sequence + "\n")
        f_write.write(line + "\n")
  f_write.close()
  
# print(break_into_kmers("TAGCTTAAAAAGCTCCTTGAACAATGGAACCTAGTTATAGGTTTCCTATTCCTTACATGTATTTGTCTTCTCCTTTTTGCCTATGCCCTCAGGTATAGGTTTTTGTTTATAATTAAGT", 30))
# clean_up_data("sars-cov-2-raw-data/SRR12844648_1.fastq", "data1.txt")
# clean_up_data("sars-cov-2-raw-data/SRR12844648_2.fastq", "data2.txt")