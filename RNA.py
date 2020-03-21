#!/usr/bin/env python3

import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser()
parser.add_argument("--fasta", "-F", help = "Fasta file to be parsed.")
# arguments
args = parser.parse_args()

    ######################################
#                 Read fasta                #
    ######################################

for record in SeqIO.parse(args.fasta, "fasta"):
    sequence = str(record.seq)
    print(">", record.id)
    print(sequence.replace("T", "U"))




	


