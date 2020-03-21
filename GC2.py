#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqUtils import GC
import os as os

os.chdir("/Users/mbrown/Downloads")

GCcont = 0
GCname = ""

file = open("rosalind_GC.txt", "r") # r for reading
for record in SeqIO.parse(file, "fasta"):
    if GCcont < GC(record.seq):
        GCcont = GC(record.seq)
        GCname = record.id

print(GCname)
print(round(GCcont,2), "%")

# second solution from 'base' python

f = open('rosalind_gc.txt', 'r')

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
print(buf)

while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()