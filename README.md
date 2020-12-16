# SARS-CoV-2 Assembled Genome

### Authors:
- Wiley Bui
- Guogeng Li
- Yunong Xia
- Weijie Zhang

### Files:
```
.
├── Graphs/
        Graphs of different k's and De Bruijn graph
├── Results/
        Results from Eulerian paths. Note: the first line of each file indicates if there exists an Eulerian path.
├── trimmomatic_outputs/
        Filters FASTQ file outputs
├── clean_up_data.py
        Cleans the data from trimmomatic outputs
├── data_1.txt
        Clean-data output from clean_up_data.py
├── data_2.txt
        Clean-data output from clean_up_data.py
├── data_covid.txt
├── eulerian_path.py
        Implements the Eulerian Path (with Eulerian Circuits)
├── graph_construct.py
        Creates De Bruijn graph
└── unit_test.py
        Multiple unit tests for Eulerian path
```

### Usage:
`python eulerian_path.py`