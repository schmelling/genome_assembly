'''
  
  Extract all orthologs from fasta file
  
  Usage: python extract <fasta_file> <output_file>
  
  Author: Nicolas Schmelling

'''
from Bio import SeqIO
import sys

def extract(fasta_file, output_file):
    with open(output_file,"w") as f:
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            if 'ortho' in seq_record.description:
                f.write(str(seq_record.description) + '\n')
                f.write(str(seq_record.seq) + '\n')
                
if __name__ == "__main__":
    fasta_file = sys.argv[1]
    output_file = sys.argv[2]
    
    extract(fasta_file, output_file) 
