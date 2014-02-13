#############################################################################
#
#   This script provides a way to split a fasta file into to subfiles
#
#   Please change the filenames for your purpose and the startswith argument
#
#   Author: Nicolas Schmelling
#
#############################################################################


new = open('1.fasta','w')
with open('test.fasta','r') as tf:
    count = 0
    for line in tf:
        if line.startswith(">DEF"):
            count += 1
        if count == 1:
            new.close()
            count = 0
            new = open('2.fasta', 'w')
        new.write(line)
new.close()
