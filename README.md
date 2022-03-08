# identifying-unique-oligomers
This repo will help you identify unique 10-mer sequences and performing multiple tasks on them
Task description 
1.	Take the ‘proteins.fasta’ file as input and produce the following tables as output: 
1.	A list of each of the unique 10mer sequences in the input file, with a count of how many times each occurs. It should be two tab-separated columns with the 10mer sequence in the first column and its counts in the second column, sorted in decreasing order by count. As a bonus, include a third column that contains an ‘X’ if the counts of the peptide are in the 20th to 30th percentile of overall counts (with the first percentile being the highest). 
Example: 
          DGTRREEFQW     35
          HHPWVWLKSS     28
          PRPRRRPRWS     5
          ...
2.	A file that contains the following summary statistics on the counts: min, max, median, mean, and variance. There should be one label and value per row, separated by a colon and a space. 
Example: 
min: 1 max: 52 median: 6 ... 

*proteins.fasta is the list of protein sequences (amino acid sequences)
*tasks.py is the final code
