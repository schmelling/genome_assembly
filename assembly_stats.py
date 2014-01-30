################################################################################################################
#
#   Calculating of [Total Assembly Length], [Total # of Contigs], [Total # of trimmed Contigs]'
#   [Min Contig Size [bp]], [Median Contig Size [bp]], [Mean Contig Size [bp]], [Max Contig Size [bp]],
#   [N50[bp] [# of Contigs]], [NG50[bp] [# of Contigs]], [N90 [bp] [# of Contigs]], [NG90 [bp] [# of Contigs]],
#   [Total # of Contigs > Average Gene Size]
#
#   This code creates an output txt file with all of the statistics
#
#   This file needs to be adjusted to your one file and genome settings
#
#   Author: Nicolas Schmelling
#
################################################################################################################

from __future__ import division
from Bio import SeqIO

# Change file name
contigsMultifasta = r'VelvetOp_assembly.fa'

# Estimated Genome Size
# Change Genome Size
genome = 86000000

contigsLength = []
trimmedLength = []
sum = 0

# Create lists for Total Length and Trimmed Length
for seq_record in SeqIO.parse(open(contigsMultifasta), 'fasta'):
    contigsLength.append(len(seq_record.seq))
    # Min Contig Length Threshold 
    # Change Threshold
    if len(seq_record.seq) > 499: 
        sum += len(seq_record.seq)
        trimmedLength.append(len(seq_record.seq))

# Sorting the Trimmed Contigs from Large to Small
trimmedLength.sort()
trimmedLength.reverse()

# Theoretic NXX and NGXX Sizes
teoN50 = sum / 2.0 
teoNG50 = genome / 2.0
teoN90 = (sum / 100)*90
teoNG90 = (genome /100)*90

# Calculating Mean Contig Size
meancontig = int(sum/len(trimmedLength))

# Calculating Median Contig Size
median = []
medcon = []

for con in trimmedLength:
    medcon.append(con)
    if len(medcon) > len(trimmedLength)/2:
        median.append(con)
        break

# Checking N50 [bp] [# of Contigs]
testSum = 0
N50 = 0
N50con = 0
for con in trimmedLength:
    testSum += con
    N50con += 1
    if teoN50 < testSum:
        N50 = con
        break
 
# Checking NG50 [bp] [# of Contigs]
testSum = 0
NG50 = 0
NG50con = 0
for con in trimmedLength:
    testSum += con
    NG50con += 1
    if teoNG50 < testSum:
        NG50 = con
        break
        
# Checking N90 [bp] [# of Contigs]
testSum = 0
N90 = 0
N90con = 0
for con in trimmedLength:
    testSum += con
    N90con += 1
    if teoN90 < testSum:
        N90 = con
        break
   
# Checking NG90 [bp] [# of Contigs]
testSum = 0
NG90 = 0
NG90con = 0
for con in trimmedLength:
    testSum += con
    NG90con += 1
    if teoNG90 < testSum:
        NG90 = con
        break
        
# Calculating # of Contigs > Average Gene Size
ags = 2000
Xkb = 0
for con in trimmedLength:
    if con > ags:
        Xkb += 1
        
        
print 'total length: ' + str(sum)
print '# of contigs: ' + str(len(contigsLength))
print '# of trimmed contigs: ' + str(len(trimmedLength))
print 'min. contig: ' + str(min(trimmedLength))
print 'median contig: ' + str(median[0])
print 'mean contig size: ' + str(meancontig)
print 'max. contig: ' + str(max(trimmedLength))
print 'N50 Length: ' + str(N50)
print 'N50 Contig: ' + str(N50con)
print 'NG50: ' + str(NG50)
print 'NG50 Contig: ' + str(NG50con)
print 'N90: ' + str(N90)
print 'N90 Contig: ' + str(N90con)
print 'NG90: ' + str(NG90)
print 'NG90 Contig: ' + str(NG90con)
print '# of contigs > 2000b: ' + str(Xkb)


out = open(contigsMultifasta + '_stats.txt', 'w')
out.write(contigsMultifasta + '\n')
out.write('total length: ' + str(sum) + '\n')
out.write('# of contigs: ' + str(len(contigsLength)) + '\n')
out.write('# of trimmed contigs: ' + str(len(trimmedLength)) + '\n')
out.write('min. contig [bp]: ' + str(min(trimmedLength)) + '\n')
out.write('median contig [bp]: ' + str(median[0]) + '\n')
out.write('mean contig size [bp]: ' + str(meancontig) + '\n')
out.write('max. contig [bp]: ' + str(max(trimmedLength)) + '\n')
out.write('N50 Length[bp]: ' + str(N50) + '\n')
out.write('N50 Contig: ' + str(N50con) + '\n')
out.write('NG50 Length[bp]: ' + str(NG50) + '\n')
out.write('NG50 Contig: ' + str(NG50con) + '\n')
out.write('N90 Length[bp]: ' + str(N90) + '\n')
out.write('N90 Contig: ' + str(N90con) + '\n')
out.write('NG90 Length[bp]: ' + str(NG90) + '\n')
out.write('NG90 Contig: ' + str(NG90con) + '\n')
out.write('# of contigs > 2000b: ' + str(Xkb) + '\n')
out.close()
