#!/usr/bin/env python3

import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser()
parser.add_argument("--fasta", "-F", help = "Fasta file to be parsed.")
# arguments
args = parser.parse_args()

    ######################################
#                 Functions                #
    ######################################

def table(string):
    freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in string:
       freq[c] = string.count(c)
    return freq

    ######################################
#                 Read fasta                #
    ######################################

for record in SeqIO.parse(args.fasta, "fasta"):
    print(record.id)
    print(table(record.seq))
