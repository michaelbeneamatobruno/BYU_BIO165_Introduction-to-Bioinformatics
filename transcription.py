
import sys
import re
#create a readable file
fasta_file= open(".:INPUT:.", "r")
#fasta_file = fasta_file.read
#makes an ouput file
output_fasta= open(".:OUTPUT.:", "w")
#give the first readline
Seqname= fasta_file.readline()

#makes a dictionary for reverse compliment
nucdictionary= {"A":"T", "T":"A", "G":"C", "C":"G"}

#while loop
while Seqname != "": 

	Seq= fasta_file.readline()
	Seq= Seq.strip()
	Seq= Seq.upper()
	Seq+="\n"
	Mystring= Seq 
	Regex= r"T"
	Replace= r"U" 
	Newstring= re.sub(Regex, Replace, Mystring)

#we need to get the complement and reverse it and put it into the output file
	output_fasta.write(Seqname)
	output_fasta.write(Newstring)
	Seqname= fasta_file.readline()
output_fasta.close()
fasta_file.close()






