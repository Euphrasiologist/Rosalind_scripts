#!/usr/bin/env python3

# argparse for command line options
import argparse
from Bio import SeqIO

# given an RNA string corresponding to a strand of mRNA
# return the protein string encoded 

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", help = "File or string containing text to be parsed.")
parser.add_argument("--fasta", "-F", help = "Fasta file to be parsed.")
# arguments
args = parser.parse_args()

# to change RNA to protein each codon from the start
# needs to be read, and assuming the open reading frame is the first 
# letter of the mRNA sequence

# thank you https://github.com/mtarbit/Rosalind-Problems/blob/master/e008-prot.py
# I did just want to get the table, but the implementation was so cool, I kept it
# so the RNAtoProt function is from that link!

RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def RNAtoProt(sequence):
	res = ''
	# i.e, 0, 3, 6 etc...
	for codon in range(0, len(sequence), 3):
		# look up the amino acid where the sequence from the 1st to the third codon
		amino_acid = RNA_CODON_TABLE[sequence[codon:codon+3]]
		# break if there is a stop codon
		if amino_acid == 'Stop':
			break
		res += amino_acid
		# return the result
	return(res)


# if --file (-f)
if args.file:
	print("Parsing file...\n")

	with open(args.file, 'r') as file:
		sequence = str(file.read())
	
	print(RNAtoProt(sequence) + "\n")

# if --fasta (-F)
if args.fasta:
	print("Parsing fasta file...\n")
	# point to a new variable for clarity
	fasta = args.fasta

	fasta_parsed = SeqIO.parse(fasta, 'fasta')

	for fastai in fasta_parsed:
		name = fastai.id
		sequence = str(fastai.seq)
		out = RNAtoProt(sequence)
		print(">", name, "\n", out)










