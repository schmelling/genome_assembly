'''
    Finding matches and no matches between a fasta and a BLAST file
    
    Usage: python find_match_2.py <fasta_file> <blast_file> <kind of sequence in blast rna/prot>
    
    Author: Nicolas Schmelling

'''
import sys
from Bio import SeqIO

def compare(fasta_file, blast_file, kind):
    RNA_hit = {}
    fasta_hit = {}
    with open(blast_file, 'r') as blast:
        
        match = open('match_'+kind+'.txt','w')
        no_match = open('no_match_'+kind+'.txt','w')
        
        for line in blast:
            RNA_hit.update({line.split()[0]:line.split()[1]})
        
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            fasta_hit.update({seq_record.record:seq_record.description})
                
        for hit in fasta_hit:
            if hit in RNA_hit:
                match.write(str(fasta_hit.get(hit)) + '\t' + str(RNA_hit.get(hit)) + '\n')
            else:
                no_match.write(str(fasta_hit.get(hit)) + '\n')
                
        match.close()
        no_match.close()
                    
if __name__ == "__main__":
    fasta_file = sys.argv[1]
    blast_file = sys.argv[2]
    kind = sys.argv[3]
    
    compare(fasta_file, blast_file, kind) 
