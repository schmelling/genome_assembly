'''
  
  This code take a parsed BLAST file and returns the best hit
  
  Usage: python best_hit.py <input_file> <output_file>

  Author: Nicolas Schmelling
  
'''

import sys

def best_hit(file, output):
    
    best = open(output, 'w')
    best.close()
    best = open(output, 'r+')
    r = open(file, 'r')
    count = []
    
    for line in r:
        if line.split('\t')[0] in count:
            continue
        else:
            best.write(line)
            count.append(line.split('\t')[0])
    best.close()
    
if __name__ == "__main__":
    file = sys.argv[1]
    output = sys.argv[2]
    
    best_hit(file, output)
