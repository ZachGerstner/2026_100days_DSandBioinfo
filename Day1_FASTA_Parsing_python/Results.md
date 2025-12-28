# Day 1 : Parsing Fasta Files

To this end I wrote the python script similar to a bash script. No functions just bare bones parse the file. 
After passing it to the grader (Gemini and colleagues) I took their feeback and introduced a function with 
several sanity checks. 

## Real Data Test

I selected a single SRR project from a study looking at the gut disbiosis in children with ASD, 
SRR16229596. Roughly 12MB of sequencing data ran on [Palmetto 2](https://docs.rcd.clemson.edu/palmetto/).

They were downloaded from ncbi via prefetch :

```shell-session
prefetch SRR16229596
```

Afterwards I used `fasterq-dump` to extract the fasta files : 
```shell-session
fasterq-dump SRR16229596
```

I then had to generate a conda environment for the script to work :

```shell-session
conda create --name 100days numpy pandas Bio pathlib
```

## Test Output

I received the following after running the following command :

```shell-session
conda activate 100days
python Parser.py /scratch/username/testseqs
```

```shell-session
ID : SRR16229596.7727
Description : SRR16229596.7727 7727 length=301
Sequence : GACTACAGGGGTATCTAATCCTGTTTGCTCCCCACACTTTCGCGCCTCAGCGTCAGTTGTCGTCCAGAAAGCCGCCTTCG
Sequence Len : 301
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ID : SRR16229596.7728
Description : SRR16229596.7728 7728 length=301
Sequence : ATCCTACGGGAGGCTGCAGTGAGGAATATTGGTCAATGGGCGAGAGCCTGAACCAGCCAAGTAGCGTGCAGGATGACGGC
Sequence Len : 301
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```