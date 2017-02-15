#DNA Analysis Toolbox ~ lab 5
#lets party
import re
import sys

#Input- input will always be fasta file, always retrieved from the command line (i.e. use sys.argv)

#Arguments that you need to code for

# -g = GC%
# -r = reverse compliment
# -s = transcription
# -t = translation
# -c = counting nucletotides

#----------------------------preliminary functions----------------------------------

#getLength function
def getLength(string):
	length= 0
	for char in string:
		length += 1
	return length

#getCount function
def getCount (string, char): 
	count= 0
	for nuc in string:
		if nuc == char:
			count += 1
	return count

#Errorchecking function
def Errorchecking(DNASeq):
	if re.search('[^ATGC]', DNASeq): 
		return "ERROR"
	else: 
		return DNASeq

#Dictionary re.search error killer function
def killallerrors(string):
	nucdictionary= {"a":"A", "c":"C", "t":"T", "g":"G", " ":"", "\t":''}
	result=""
	for nuc in string:
		if re.search('[actg]', nuc):
			result+= nucdictionary[nuc]
		elif re.search('\s', nuc):
			result+= nucdictionary[nuc]
		elif re.search('\t', nuc):
			result+= nucdictionary[nuc]
		else:
			result+= nuc
	return result

#codon dictionary function
def loadCodonsDict(codon_filename):
	codons= {}
	file= open(codon_filename, 'r')
	for protein in file:
		protein= protein.strip()
		protein= protein.split("\t")
		codons[protein[0]]=protein[1]
	return codons

#----------------------------Option Functions---------------------------------	

#calcGC function
def calcGC(header, valid_sequence):
	seqlength= getLength(valid_sequence)
	Ccount= getCount(valid_sequence, 'C')	
	Gcount= getCount(valid_sequence, 'G')
	percentC= (100 * float(Ccount) / seqlength)
	percentG= (100 * float(Gcount) / seqlength)
	GC = str(percentC + percentG)
	return header + '\t' + GC + '%\n'

#reverse complement function
def revComp(header, valid_sequence):
	nucdictionary= {"A":"T", "T":"A", "G":"C", "C":"G"}
	result = ''	
	for nuc in valid_sequence:
		result += nucdictionary[nuc]
	reverse_complement = result[::-1]
	return header + '\n' + reverse_complement + '\n'

#transcription function
def transcribe(header, valid_sequence):
	Mystring= re.sub('T', 'U', valid_sequence)
	return header + '\n' + Mystring + '\n'

#translation function
def translate(header, valid_sequence, codons):
	Newstring= re.sub('T', 'U', valid_sequence)
	Newstring= iter(Newstring)
	proteinseq= '' 
	for nuc in Newstring:
		codon= nuc + Newstring.next()+ Newstring.next()
		pep= codons[codon]
		if pep== '*':
			return header + '\n' + proteinseq + '\n'	
		else:
			proteinseq += pep
	return header + '\n' + proteinseq + '\n'

#Count nucleotides function
def countNucs(header, goodseq):
	seqlength= getLength(goodseq)
	seqcountA= str(getCount(goodseq, 'A'))
	seqcountC= str(getCount(goodseq, 'C'))
	seqcountG= str(getCount(goodseq, 'G'))
	seqcountT= str(getCount(goodseq, 'T'))
	percentA= str((100 * float(seqcountA) / seqlength))
	percentC= str((100 * float(seqcountC) / seqlength))
	percentG= str((100 * float(seqcountG) / seqlength))
	percentT= str((100 * float(seqcountT) / seqlength))
	return header + '\t' + str(seqlength) + '\t' +  seqcountA + '(' + percentA +'%)\t' + seqcountC + '(' + percentC + '%)\t' + seqcountG + '(' + percentG + '%)\t' + seqcountT + '(' + percentT + '%)\n'

#----------------------Arguments and argument errors----------------------------------

#Incorrect number of arguments error statement
if getLength(sys.argv) < 4:
	print 'Error: USAGE: python lab5.py: option input.fasta output.txt\n\tAvailable options:\n\t\t-g GC%\n\t\t-r reverse complement\n\t\t-s transcription\n\t\t-t translation\n\t\t-c count nucleotides\n'
	sys.exit()
elif sys.argv[1] == '-t':
	if getLength(sys.argv) != 5:
		print 'Error: USAGE: python lab5.py: option input.fasta output.txt\n\tAvailable options:\n\t\t-g GC%\n\t\t-r reverse complement\n\t\t-s transcription\n\t\t-t translation\n\t\t-c count nucleotides\n'
		sys.exit()
elif re.search('-[grsc]', sys.argv[1]):
	if getLength(sys.argv) != 4:
		print 'Error: USAGE: python lab5.py: option input.fasta output.txt\n\tAvailable options:\n\t\t-g GC%\n\t\t-r reverse complement\n\t\t-s transcription\n\t\t-t translation\n\t\t-c count nucleotides\n'
		sys.exit()
else:
	print 'Error: USAGE: python lab5.py: option input.fasta output.txt\n\tAvailable options:\n\t\t-g GC%\n\t\t-r reverse complement\n\t\t-s transcription\n\t\t-t translation\n\t\t-c count nucleotides\n'
	sys.exit()

#----------------input and output------------------------

infile= open(sys.argv[2], 'r')

if sys.argv[1] == '-t':
	outfile= open(sys.argv[4], 'w')
else:
	outfile= open(sys.argv[3], 'w')
#---------------------Options--------------------------
if sys.argv[1] == '-g':
	outfile.write('ID\tGC%\n') 
elif sys.argv[1] == '-c':
	outfile.write('ID\tLength\tA(%A)\tC(%C)\tG(%G)\tT(%T)\n')
for line in infile:
	line= line.strip()
	if re.search('[gc]', sys.argv[1]):
		line = re.sub('>', '', line)
	Seq= infile.next()
	Seq= Seq.strip()
	Seq= killallerrors(Seq)	
	Seq= killallerrors(Seq)	
	Seq= Errorchecking(Seq)
	if Seq == "ERROR" and re.search('[gc]', sys.argv[1]):
		outfile.write(line + '\tERROR\n')
	elif Seq == "ERROR" and re.search('[rst]', sys.argv[1]):
		outfile.write(line + '\nERROR\n')
	elif sys.argv[1] == '-g':
		GCarg = calcGC(line, Seq)
		outfile.write(GCarg)	
	elif sys.argv[1] == '-r':
		revcompliment= revComp(line, Seq)
		outfile.write(revcompliment)	
	elif sys.argv[1] == '-s':
		transcription = transcribe(line, Seq)
		outfile.write(transcription)	
	elif sys.argv[1] == '-t':
		cod= loadCodonsDict(sys.argv[3])
		transfinal = translate(line, Seq, cod)
		outfile.write(transfinal)	
	elif sys.argv[1] == '-c':
		countthemnucs = countNucs(line, Seq)
		outfile.write(countthemnucs)

