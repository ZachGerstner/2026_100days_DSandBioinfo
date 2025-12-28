# Day 2 : Determining GC content with Biopython

This stage was faily straight forward. Taking the script from day 1 
I added a single line using the `gc_fraction` function from biopython.
This function easily determines the fraction of GC content in a sequence 
as shown in my test case result below. 

```shell-session
Parsing File : TestSeq.fasta
--------------------------------------------------------------------------------
ID : TestSeq-001
Description : TestSeq-001 test seq1
Sequence : ATTTGGGCCCCCTTCTCCCGGAAAATAATAGCT
Sequence Len : 33
GC Fraction : 0.48484848484848486
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ID : TestSeq-002
Description : TestSeq-002 test seq2
Sequence : TTGCAAATTCCTCCCAAAGAGATATATCCCATC
Sequence Len : 33
GC Fraction : 0.3939393939393939
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

Its important to use `gc_fraction` over the traditional `GC` command as it is 
depricated in the newer versions of Biopython.