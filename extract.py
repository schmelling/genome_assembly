'''
  
  Extract special sequences from fasta file. You can specify which sequences get extracted by using the a separator.
  
  Usage: python extract <fasta_file> <output_file> <separator>
  
  Author: Nicolas Schmelling

'''
from Bio import SeqIO
import sys

def extract(fasta_file, output_file, separator):
    with open(output_file,"w") as f:
        extract_seqs = []
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            if separator in seq_record.description:
                extract_seqs.append(seq_record)
                
        SeqIO.write(extract_seqs, f, "fasta")
                
if __name__ == "__main__":
    fasta_file = sys.argv[1]
    output_file = sys.argv[2]
    separator = sys.argv[3]
    
    extract(fasta_file, output_file, separator) 
