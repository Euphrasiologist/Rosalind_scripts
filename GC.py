#!/usr/bin/env python3

# Computing GC content
# percentage of symbols that are C or G!

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
    freq = {'C': 0, 'G': 0}
    for c in string:
       freq[c] = string.count(c)
    return freq

    ######################################
#                 Read fasta                #
    ######################################

for seq_record in SeqIO.parse(args.fasta, "fasta"):
	x = table(seq_record.seq)
	names = {'G', 'C'}
	lst = { key:value for key,value in x.items() if key in names}
	sol = sum(lst.values())/sum(x.values())*100 

print(">",seq_record.id)
print(round(sol, 4))






