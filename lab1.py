#/usr/bin/env python
import sys
import re

#First lab, prompts for a DNA sequence, then shows nucleotide composition

#Ask for a DNA Sequence, change to uppercase, remove spaces, system exit if return key is hit w/o sequence or if not ATGC
DNAseq1= raw_input("Sequence 1: ")
DNAseq1= DNAseq1.upper()
DNAseq1= DNAseq1.replace(" ","")
SeqLength1= len(DNAseq1)
if SeqLength1== 0:
	print "You must enter a DNA sequence"
	sys.exit()
if re.search('[^ATGC]',DNAseq1):
	print "ERROR: Invalid DNA sequence"
	sys.exit()

DNAseq2= raw_input("Sequence 2: ")
DNAseq2= DNAseq2.upper()
DNAseq2= DNAseq2.replace(" ","")
SeqLength2= len(DNAseq2)
if SeqLength2== 0:
	print "You must enter a DNA sequence"
	sys.exit()
if re.search('[^ATGC]',DNAseq2):
	print "ERROR: Invalid DNA sequence"
	sys.exit()

DNAseq3= raw_input("Sequence 3: ")
DNAseq3= DNAseq3.upper()
DNAseq3= DNAseq3.replace(" ","")
SeqLength3= len(DNAseq3)
if SeqLength3== 0:
	print "you must enter a DNA sequence"
	sys.exit()
if re.search('[^ATGC]',DNAseq3):
	print "ERROR: Invalid DNA sequence"
	sys.exit()

#Total Sequence length
TotalSeqLength= SeqLength1+SeqLength2+SeqLength3

#Sequence Lengths
print "Sequence 1:", SeqLength1
print "Sequence 2:", SeqLength2
print "Sequence 3:", SeqLength3

#Print sequence
SeqPrint= DNAseq1+DNAseq2+DNAseq3
print SeqPrint 

#Define Nucleotides
NumberC= float(SeqPrint.count("C")) 
NumberG= float(SeqPrint.count("G"))

#Print GC content percentage
print "%f" % (100 * (NumberG+NumberC) / TotalSeqLength)










