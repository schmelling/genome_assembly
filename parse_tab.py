import sys

def blast_parse(infile, e, output):
    
    input = open(infile, 'r')
    output = open(output, 'w')
    output.write('Query id\tSubject id\t% identity\talignment length\tmismatches\tgap openings\tq. start\tq. end\ts. start\ts. end\te-value\tbit score' + '\n')
    
    for line in input:
        if float(line.split()[10]) < e:
            output.write(line)
    
    output.close()
    
    
if __name__ == "__main__":
    infile = sys.argv[1]
    e = float(sys.argv[2])
    output = sys.argv[3]
    
    blast_parse(infile, e, output)
