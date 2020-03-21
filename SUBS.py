#!/usr/bin/env/ python3

# sets the working directory
import argparse
from Bio import SeqIO
import re

parser = argparse.ArgumentParser()
parser.add_argument("--fasta", "-F", help = "First fasta file to be parsed.")
parser.add_argument("--motif", "-m", type=str, help = "Motif to be found in the fasta file")
# arguments
args = parser.parse_args()

# motif to find
t = args.motif
# create the regex object
t2 = "(?=" + t + ")"

for seq_record in SeqIO.parse(args.fasta, "fasta"):
	sol = [m.start() + 1 for m in re.finditer(t2, str(seq_record.seq))]

print(' '.join(str(x) for x in sol))