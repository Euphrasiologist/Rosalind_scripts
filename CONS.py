#!/usr/bin/env/ python3

# sets the working directory
import argparse
from Bio import SeqIO
import re

parser = argparse.ArgumentParser()
parser.add_argument("--fasta", "-F", help = "First fasta file to be parsed.")
# arguments
args = parser.parse_args()


    ######################################
#                 Read fasta                #
    ######################################

record_dict = SeqIO.index(args.fasta, "fasta")
seq_len = [len(i) for i in record_dict.values()][1]

Count_A = []
Count_C = []
Count_G = []
Count_T = []

for base in range(0, seq_len):
    
    current_record = []

    for record in record_dict.values():
        current_record.append(record[base])
        As = current_record.count('A')
        Cs = current_record.count('C')
        Gs = current_record.count('G')
        Ts = current_record.count('T')
    
    Count_A.append(str(As))
    Count_C.append(str(Cs))
    Count_G.append(str(Gs))
    Count_T.append(str(Ts))

consensus = []

convert = {0:'A',
           1:'C',
           2:'G',
           3:'T'}

for count in zip(Count_A, Count_C, Count_G, Count_T):
    consensus.append(convert[count.index(max(count))])
print(''.join(consensus))

print('A: ' + ' '.join(Count_A))
print('C: ' + ' '.join(Count_C))
print('G: ' + ' '.join(Count_G))
print('T: ' + ' '.join(Count_T))
