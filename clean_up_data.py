def clean_up_data(filename, output_file):
  """
  clean_up_data function picks only the sequences from the
  filename, and puts the results to its output_file
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
      f_write.write(current_sequence + "\n")
  f_write.close()
  
clean_up_data("trimmomatic_outputs/output_SE_read1.fq", "data_1.txt")
clean_up_data("trimmomatic_outputs/output_SE_read2.fq", "data_2.txt")