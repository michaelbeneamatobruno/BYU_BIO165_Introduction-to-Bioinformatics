#lab3 - translation

import re
import sys

def loadCodonsDict(codon_filename):
	codons= {}
	file= open(codon_filename, 'r')
	for protein in file:
		protein= protein.strip()
		protein= protein.split("\t")
		codons[protein[0]]=protein[1]
	return codons
	
#calling all shadies, will the real shady please stand up
codons= loadCodonsDict('.:CODON:.')

#open input and output files
output_fasta= open('.:OUTPUT:.', 'w')
fasta_file= open('.:INPUT:.', 'r')
Seqname= fasta_file.readline()
while Seqname != "": 
	output_fasta.write(Seqname) #give the first readline, the one with a >
#spaces, lowercase, error statement, replace T's with U's
	string= fasta_file.readline()
	string= string.strip()
	string= string.upper()
	string= string.replace(" ","")
	if re.search('[^ATGC]', string):
		output_fasta.write("ERROR" + '\n')
	else:
		Newstring= re.sub('T', 'U', string)
		Newstring= iter(Newstring) #have our way with Newstring
		seq= Newstring 
		proteinseq= '' #make a blank line
#for loop creating the peptide from 3 nucleotides
		for nuc in seq:
			codon= nuc+ seq.next()+ seq.next()
			pep= codons[codon]
			if pep== '*':
				output_fasta.write(proteinseq + '\n')
				break
			else:
				proteinseq += pep	
		
#pull out the next Seqname	
	Seqname= fasta_file.readline()
#finish up by closing the program
output_fasta.close()
fasta_file.close()






