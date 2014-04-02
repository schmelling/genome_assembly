'''
    Finding matches and no matches between a BLAST and a BLAT file

    Usage: python find_match.py <blat_file> <blast_file> <kind of sequence rna/prot>

    Author: Nicolas Schmelling

'''
import sys

def compare(blat_file, blast_file, kind):

    blast_ID = {}
    blat_ID = {}

    BLAT = open(blat_file, 'r')
    for line in BLAT.read().splitlines():
            blat_ID.update({line.split(' ', 1)[0]:line.split('\t')[1]})

    BLAST = open(blast_file, 'r')
    for line in BLAST.read().splitlines():
            blast_ID.update({line.split(' ', 1)[0]:line.split('\t')[1]})
    
    BLAT.close()
    BLAST.close()
    
    match = open('match_'+kind+'.txt','w')
    no_match = open('no_match_'+kind+'.txt','w')

    for a in blat_ID:
        if a in blast_ID:
            match.write(str(a)+'\t'+str(blat_ID.get(a))+'\t'+str(blast_ID.get(a))+'\n')
        else:
            no_match.write(str(a)+'\t'+str(blat_ID.get(a))+'\n')

    match.close()
    no_match.close()

if __name__ == "__main__":
    blat_file = sys.argv[1]
    blast_file = sys.argv[2]
    kind = sys.argv[3]

    compare(blat_file, blast_file, kind)
