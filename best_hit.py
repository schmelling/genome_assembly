'''
  
  This code take a parsed BLAST file and returns the best hit,
  if the best hit is 'hypothetical' or 'predicted' the code also returns the best hit with a know function
  
  Usage: python best_hit.py <input_file> <output_file> <best or best+>

  Author: Nicolas Schmelling
  
'''

import sys

def best_hit(file, output, option):
    
    best = open(output, 'w')
    r = open(file, 'r')
    list = []
    list2 = []
    count = 0
    
    for line in r:
        if line.split('\t')[0] in list:
            if option == 'best+':
                if 'hypothetical' in line.split('\t')[1]:
                    continue
                elif 'predicted' in line.split('\t')[1]:
                    continue
                elif line.split('\t')[0] in list2:
                    continue
                else:
                    best.write(line)
                    list2.append(line.split('\t')[0])
        else:
            best.write(line)
            list.append(line.split('\t')[0])
            
    best.close()
    
if __name__ == "__main__":
    file = sys.argv[1]
    output = sys.argv[2]
    
    best_hit(file, output)
