'''

  Separates the strand specific contigs from each other, so Gimme can work with each file separately.
  
  https://github.com/ged-lab/gimme

  Usage: python parse_psl.py <psl file>

  Author: Nicolas Schmelling

'''

import sys

def psl_parse(file):
    minus = open('minus_strand_seq.psl', 'w')
    plus = open('plus_strand_seq.psl', 'w')
    with open(file, 'rb') as infile:
        hits = infile.read().split('\n')
        for line in hits:
            if len(line) >= 19:
                if '+' in line:
                    plus.write(line.lower())
                    plus.write('\n')
                elif '-' in line:
                    minus.write(line.lower())
                    minus.write('\n')
    minus.close()
    plus.close()
    
if __name__ == "__main__":
    file = sys.argv[1]
    
    psl_parse(file)
