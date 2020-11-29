# Finding Variable Genomic Regions

## Wiley Bui | buixx206@umn.edu | 5368469

## How to Run Variable Genomic Regions
```python3 variable_genomic_regions.py <INPUT_FILE>```, such as
**```python3 variable_genomic_regions.py Homework4-seqs-with-primers.fna```**

## Files
```
├── Homework4-seqs-with-primers.fna
            Provided file of gene ids and sequences.
├── solution-problem-1.txt
            Contains the fraction of conserved bases at each position, one per line.
├── solution-problem-2.pdf
            Visualization: plot of smoothed out data from % sequence identity vs gene position
├── solution-problem-3.txt
            Contains the start and end position of each variable region in two tab-delimited columns
├── solution-problem-4.pdf
            Visualization of solution-problem-3.txt
└── variable_genomic_regions.py
            Source code to generate the previous 4 files.
```

## Python Dependencies
- numpy
- matplotlib.pyplot