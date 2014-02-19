#############################################################################
#
#   This script provides a way to parse a blast output text files
#
#   Please change the filenames for your purpose 
#
#   Author: Nicolas Schmelling
#
#############################################################################


result_handle = open("Trinity.blast.txt")

from Bio.Blast import NCBIStandalone
blast_parser = NCBIStandalone.BlastParser()
blast_iterator = NCBIStandalone.Iterator(result_handle, blast_parser)
blast_record = next(blast_iterator)

output = open('RNA_BLAST_result.txt', 'w')
output.write('query title , alignment title , length , e value' + '\n')
for blast_record in blast_iterator:
    E_VALUE_THRESH = 0.04
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                output.write(str(blast_record.query) + ',')
                output.write(str(alignment.title) + ',')
                output.write(str(alignment.length) + ',')
                output.write(str(hsp.expect) + '')
                output.write('\n')


output.close()
