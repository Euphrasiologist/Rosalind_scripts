#!/usr/bin/env python3


import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser()
parser.add_argument("--fasta", "-F", help = "Fasta file to be parsed.")
# arguments
args = parser.parse_args()

    ######################################
#                 Dictionary                #
    ######################################

# define the dictionary
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

    ######################################
#                 Read fasta                #
    ######################################

for record in SeqIO.parse(args.fasta, "fasta"):
    reverse_complement = "".join(complement.get(i) for i in reversed(record))
    print(">", record.id)
    print(reverse_complement)


