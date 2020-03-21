#!/usr/bin/env python3

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("--fasta1", "-1", help = "First fasta file to be parsed.")
parser.add_argument("--fasta2", "-2", help = "Second fasta file to be parsed.")
# arguments
args = parser.parse_args()

    ######################################
#                 Read fasta                #
    ######################################

seq_record1 = SeqIO.read(args.fasta1, "fasta")
seq_record2 = SeqIO.read(args.fasta2, "fasta")

s = []
for (a, b) in zip(seq_record1, seq_record2):
	s.append(a!=b)

print(sum(s))

# one liner print(sum([a != b for a, b in zip(seq_record1.seq, seq_record2.seq)]))