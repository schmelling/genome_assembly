'''

  Script to compare four different blastn transcript to transcript results by mapping e-values against the main
  transcript of interest. Produces a csv file.
  
  Usage: python transcript_comparison.py <transcript fasta> <blastn result 1> <blastn result 2> <blastn result 3> <output>

  Author: Nicolas Schmelling
  
'''

import sys
import decimal

def transcript_comparison(file1, file2, file3, file4, output):
    with open(file1, 'r') as Abi:
        Amu = open(file2, 'r')
        Ath = open(file3,'r')
        Vvo = open(file4,'r')
        TRANS = open(output,'w')
        TRANS.write(',A.muscaria,A.thiersii,V.volvaces\n')
        namesB = []
        namesM = {}
        namesT = {}
        namesV = {}
        for line in Abi:
            if line.startswith('>'):
                namesB.append(line.replace('>','').split(' ')[0])
        for line in Amu:
            namesM.update({line.split()[0]:decimal.Decimal(line.split()[10]).log10()})
        for line in Ath:
            namesT.update({line.split()[0]:decimal.Decimal(line.split()[10]).log10()})
        for line in Vvo:
            namesV.update({line.split()[0]:decimal.Decimal(line.split()[10]).log10()})

        for name in namesB:
            TRANS.write(name + ',')
            if name in namesM:
                TRANS.write(str(namesM[name]))
                TRANS.write(',')
            if name not in namesM:
                TRANS.write('0,')
            if name in namesT:
                TRANS.write(str(namesT[name]))
                TRANS.write(',')
            if name not in namesT:
                TRANS.write('0,')
            if name in namesV:
                TRANS.write(str(namesV[name]))
                TRANS.write('\n')
            if name not in namesV:
                TRANS.write('0\n')

        Amu.close()
        Ath.close()
        Vvo.close()


if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    file4 = sys.argv[4]
    output = sys.argv[5]
