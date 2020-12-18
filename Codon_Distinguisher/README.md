# Genomic Data

## How to run count_codons

```bat
$ python count_codons.py data/SARS-CoV-2_whole_genome.fna data_outputs/whole_genome_output.csv
$ python count_codons.py data/SARS-CoV-2_separate_genes.fna data_outputs/separate_genes_output.csv
```


## Files

```
.
├── Amino_Acid_vs_Its_Frequency_Barplot.pdf
|           Barplot comparing amino acid counts between 
|           separate genes and a whole genome (Question #6)
├── Codon_vs_Its_Frequency_Barplot.pdf
|           Barplot comparing codon counts between 
|           separate genes and a whole genome (Question #5)
├── Question7.txt
|           Answer for Question #7
├── Requirements.pdf
|           Requirements for this project
├── count_codons.py
|           Python file to count the frequencies of codons
├── data
│   ├── SARS-CoV-2_separate_genes.fna
|   |       Given separate genes
│   ├── SARS-CoV-2_whole_genome.fna
|   |       Given whole genome
│   └── test_genome.fna
|           Made-up genome (Question #3)
└── data_outputs
    ├── SARS-CoV-2_separate_genes_actual_answer.csv
    |       Frequency of codons from SARS-CoV-2_separate_genes.fna (Question #2, #4)
    ├── SARS-CoV-2_whole_genome_actual_answer.csv
    |       Frequency of codons from SARS-CoV-2_whole_genome.fna (Question #2, #4)
    ├── test_genome_actual_answer.csv
    |       Actual frequency of codons from test_genome.fna (Question #3)
    └── test_genome_expected_answer.csv
            Expected frequency of codons from test_genome.fna
```