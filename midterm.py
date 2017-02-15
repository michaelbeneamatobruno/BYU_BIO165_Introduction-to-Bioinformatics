#/usr/bin/env python
import sys
import re

print "MLH1"
print "PMS2"
print "MSH6"
print "TGFBR2"
print "MLH3"
print "MSH2"
print "EPCAM"

print "Which gene would you like to know about?"
Gene= raw_input("Gene: ")
Gene= Gene.upper()
if re.search ('MLH1', Gene):
	print "MLH1 is located on chromosome 3"
	print "The MLH1 gene codes for a DNA repair protein. The protein MLH1 codes for helps fix mistakes during DNA replication in preparation for cell division. The MLH1 protein joins with the PMS2 protein to form a protein complex. This complex repairs DNA by removing sections of incorrect DNA and replacing the section with a corrected sequence."
elif re.search ('PMS2', Gene): 
	print "PMS2 is located on chromosome 7"
	print  "The PMS2 gene codes for a DNA repair protein. The protein PMS2 codes for helps fix mistakes during DNA replication in preparation for cell division. The PMS2 protein joins with the MLH1 protein to form a protein complex. This complex repairs DNA by removing sections of incorrect DNA and replacing the section with a corrected sequence."
elif re.search ('MSH6', Gene):
	print "MSH6 is located on chromosome 2"
	print "The MSH6 gene codes for a DNA repair protein. The protein MSH6 codes for helps fix mistakes during DNA replcation in preparation for cell division. The MSH6 protein joins with the MSH2 protein to form a protein complex. This complex identifies areas where mistakes have been made during DNA replication. The MSH6 gene is a member of the mismatch repair genes." 
elif re.search ('TGFBR2', Gene):
	print "TGFBR2 is located on chromosome 3"
	print "The TGFBR2 gene provides instructions for making the protein transforming growth factor-beta receptor type 2. This protein is involved in signal transduction and can affect cell growth and division."
elif re.search ('MLH3', Gene):
	print "MLH3 is located on chromosome 14"
	print "The MLH3 gene codes for a protein that maintains genomic integrity during DNA replication and meiotic recombination. Mutations in this gene often result in tumors. The MLH3 gene is a member of the DNA mismatch repair genes."
elif re.search ('MSH2', Gene):
	print "MSH2 is located on chromosome 2"
	print"The MSH2 gene codes for a DNA repair protein. The protein MSH2 codes for helps fix mistakes during DNA replcation in preparation for cell division. The MSH2 protein joins with either the MSH6 or the MSH3 protein to form a protein complex. This complex identifies areas where mistakes have been made during DNA replication. The MSH2 gene is a member of the mismatch repair genes." 
elif re.search ('EPCAM', Gene):
	print "EPCAM is located on chromosome 2"
	print "The EPCAM gene codes for a protein known as the epithelial cellular adhesion molecule. This protein is involved in cell adhesion and cell signaling. The EPCAM gene's regular function, however, has little to do with Lynch Syndrome. A mutated form of EPCAM can inactivate the MSH2 gene, which leads to impaired DNA repair."
else:
	print "ERROR: You must choose a valid gene"
	sys.exit()












