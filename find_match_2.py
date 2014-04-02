'''
    Finding matches and no matches between a fasta and a BLAST file
    
    Usage: python find_match.py <fasta_file> <blast_file> <kind of sequence in blast rna/prot>
    
    Author: Nicolas Schmelling

'''
import sys

def compare(fasta_file, blast_file, kind):
    RNA_hit = {}
    fasta_hit = {}
    with open(fasta_file, 'r') as infile:
        blast = open(blast_file)
        
        match = open('match_'+kind+'.txt','w')
        no_match = open('no_match_'+kind+'.txt','w')
        
        for line in blast:
            RNA_hit.update({line.split()[0]:line.split()[1]})
        
        for line in infile:
            if line.startswith('>') and len(line) > 100:
                fasta_hit.update({line.split(' ',1)[0].replace('>',''):line.split(' ',1)[1].replace('\n','')})
                
        for hit in fasta_hit:
            if hit in RNA_hit:
                match.write(str(hit) + '\t' + str(fasta_hit.get(hit)) + '\t' + str(RNA_hit.get(hit)) + '\n')
            else:
                no_match.write(str(hit) + '\t' + str(fasta_hit.get(hit)) + '\n')
                
        match.close()
        no_match.close()
                    
if __name__ == "__main__":
    fasta_file = sys.argv[1]
    blast_file = sys.argv[2]
    kind = sys.argv[3]
    
    compare(fasta_file, blast_file, kind) 
