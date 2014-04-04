'''
  
  Extract special sequences from fasta file. You can specify which sequences get extracted by using the a separator.
  
  Usage: python extract <fasta_file> <output_file> <separator>
  
  Author: Nicolas Schmelling

'''
from Bio import SeqIO
import sys

def extract(fasta_file, output_file, separator):
    with open(output_file,"w") as f:
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            if separator in seq_record.description:
                f.write(str(seq_record.description) + '\n')
                f.write(str(seq_record.seq) + '\n')
                
if __name__ == "__main__":
    fasta_file = sys.argv[1]
    output_file = sys.argv[2]
    separator = sys.argv[3]
    
    extract(fasta_file, output_file, separator) 
