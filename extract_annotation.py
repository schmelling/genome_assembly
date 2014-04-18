
from Bio import SeqIO
import sys

def extract(fasta_file, output_file):
    with open(output_file,"w") as f:
        orthologs = []
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            if len(seq_record.description) > 100:
                orthologs.append(seq_record)

        SeqIO.write(orthologs, f, "fasta")

if __name__ == "__main__":
    fasta_file = sys.argv[1]
    output_file = sys.argv[2]

    extract(fasta_file, output_file)
