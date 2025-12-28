from Bio.SeqUtils import gc_fraction
from Bio import SeqIO
import sys
from pathlib import Path

def fasta_dir_parser(directory_path):
    # convert the filepath string to a path object
    filepath = Path(directory_path)
    # find fastas and sanity check
    fasta_files = list(filepath.glob("*.fasta")) + list(filepath.glob("*.fa"))
    if not fasta_files:
        print(f"Failed to identify any Fasta files in the specified directory!")
        return
    
    # parse the files
    for fasta in fasta_files:
        print(f"Parsing File : {fasta.name}")
        print(f"-" * 80)
        for sequence in SeqIO.parse(fasta, "fasta"):
            print(f"ID : {sequence.id}")
            print(f"Description : {sequence.description}")
            tmp = sequence.seq
            concatseq = str(tmp)[:80]
            print(f"Sequence : {concatseq}")
            print(f"Sequence Len : {len(sequence.seq)}")
            print(f"GC Fraction : {gc_fraction(sequence.seq)}")
            print("~" * 80)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fasta_dir_parser(sys.argv[1])
    else:
        print("Error : No Directory provided!")
        print("Usage : python GC_Calc.py <dir path>")