#lab 4: Counting nucleotides. 
#complete the DNA toolbox. input is a fasta file of DNA sequences, but output is a tab delimited file with the name of the sequences, the sequence lengthm the number of A's/ % A's, T's, G's and C's.

import re
import sys

#Error checking is the same as the last lab, create a function for error checking
def Errorchecking(DNASeq):
	DNASeq= DNASeq.strip()
	DNASeq= DNASeq.upper() #Upper and lower case nucleotides
	DNASeq= DNASeq.replace(" ","") #Spaces between character
	if re.search('[^ATGC]', DNASeq): #If not ATGC, return Error
		return "ERROR"
	else: #if ATGC, return Seq
		return DNASeq
#getLength function
def getLength(string):
#this function needs to calculate the legnth of each DNA sequence.
	length= 0
	for char in string:
		length += 1
	return length

#getCount function
def getCount (string, char): 
#this function needs to calculate the number and percentages of ACTG's
#cannot call getLength inside this function
	count= 0
	for nuc in string:
		if nuc == char:
			count += 1
	return count

#if there's not two arguments (sys.argv included), print ERROR: Incorrect number of arguments
if getLength(sys.argv) != 3:
	print "ERROR: Incorrect number of arguments"
	sys.exit()

#input will be a fasta file and will be specified with the argv list
#the number of command line parameters must be 2 command line parameters
infile= open(sys.argv[1], 'r')
outfile= open(sys.argv[2], 'w')

#header

outfile.write('ID\tLength\tA(%A)\tC(%C)\tG(%G)\tT(%T)\n')

#actual code
for line in infile:
	line = line.replace('>', '')
	line= line.strip()
	outfile.write(line + '\t')
	Seq= infile.next()
	goodseq= Errorchecking(Seq)
	if goodseq== "ERROR":
		outfile.write('ERROR' + '\n')
	else:
		seqlength= getLength(goodseq)
		outfile.write(str(seqlength) + '\t')
		seqcountA= getCount(goodseq, 'A')
		seqcountC= getCount(goodseq, 'C')
		seqcountG= getCount(goodseq, 'G')
		seqcountT= getCount(goodseq, 'T')
		percentA= (100 * float(seqcountA) / seqlength)
		percentC= (100 * float(seqcountC) / seqlength)
		percentG= (100 * float(seqcountG) / seqlength)
		percentT= (100 * float(seqcountT) / seqlength)
		outfile.write(str(seqcountA) + '(' + str(percentA) + '%)\t')
		outfile.write(str(seqcountC) + '(' + str(percentC) + '%)\t')
		outfile.write(str(seqcountG) + '(' + str(percentG) + '%)\t')
		outfile.write(str(seqcountT) + '(' + str(percentT) + '%)\n')
