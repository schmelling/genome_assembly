import csv

def compare(blat_file, blast_file, kind):
    
    blast_rnaID = []
    blast_descriptionID = []
    blat_rnaID = []
    blat_genID = []
    
    with open(blat_file) as f:
        read = csv.reader(f, delimiter='\t')
        for ele in read:
            blat_genID.append(ele[1])
            
    BLAT = open(blat_file)
    for line in BLAT.read().splitlines():
            query = line.split(' ', 1)[0]
            blat_rnaID.append(query)
            
    with open(blast_file) as f:
        read = csv.reader(f, delimiter='\t')
        for ele in read:
            blast_descriptionID.append(ele[1])
            
    BLAST = open(blast_file)
    for line in BLAST.read().splitlines():
            query = line.split(' ', 1)[0]
            blast_rnaID.append(query)
            
    match = open('match_'+kind+'.txt','w')
    no_match = open('no_match_'+kind+'.txt','w')
    
    blat_dict = dict(zip(blat_rnaID, blat_genID))
    blast_dict = dict(zip(blast_rnaID, blast_descriptionID))
    
    for a in blat_dict:
        if a in blast_dict:
            match.write(str(a)+'\t'+str(blat_dict.get(a))+'\t'+str(blast_dict.get(a))+'\n')
        else:
            no_match.write(str(a)+'\t'+str(blat_dict.get(a))+'\n')
    
    match.close()
    no_match.close()
