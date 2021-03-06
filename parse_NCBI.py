'''

   This script provides a way to parse a BLAST/BLAT (if in NCBI Blast format) output.txt files
   The output file contains the query ID, description, length and the e value
   
   Usage: python parse.py <blast file> <e value> <output file>

   Author: Nicolas Schmelling

'''

from Bio.Blast import NCBIStandalone
import sys

def blast_parse(file, e, output):

    result_handle = open(file)
    
    blast_parser = NCBIStandalone.BlastParser()
    blast_iterator = NCBIStandalone.Iterator(result_handle, blast_parser)
    blast_record = next(blast_iterator)
    
    output = open(output, 'w')
    output.write('query title\tdescription\tlength\te value' + '\n')
    for blast_record in blast_iterator:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < e:
                    output.write(str(blast_record.query[:18]) + ' \t')
                    output.write(str(alignment.title) + '\t')
                    output.write(str(alignment.length) + '\t')
                    output.write(str(hsp.expect) + '')
                    output.write('\n')
    
    
    output.close()

if __name__ == "__main__":
    file = sys.argv[1]
    e = float(sys.argv[2])
    output = sys.argv[3]
    
    blast_parse(file, e, output)
