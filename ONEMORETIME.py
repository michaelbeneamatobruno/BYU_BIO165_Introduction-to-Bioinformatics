import re
import sys


#use a sys.argv for our output file, our genefile(called CORDfile here), and our outfile(where we'll be writing to)

output = open(sys.argv[1], 'r')
CORDfile = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], 'w')

#make a bunch of lists for all the information we're going to have, we probably don't need them all, but might as well be on the safe side

CHROMlist = []
POSlist = []
IDlist = []
REFlist = []
VARlist = []
CCHROMlist = []
CCORD1list = []
CCORD2list = []
GENElist = []
CORDlist = []
FullCORDlist = []



# a for loop for our output, we're making a whole bunch of lists out of all of the info we have
for line in output:

	line.strip()
	CHROM = line.split('\t')[0];
	CHROMlist.append(CHROM)
	POS = line.split('\t')[1];
	POSlist.append(int(POS))
	ID = line.split('\t')[2];
	IDlist.append(ID)
	REF = line.split('\t')[3];
	REFlist.append(REF)
	VAR = line.split('\t')[4];
	VARlist.append(VAR)

#A for loop for our genefile
for line2 in CORDfile:
	line2 = line2.strip()
	CCHROM = line2.split('\t')[0];
	CCORD1 = line2.split('\t')[1];
	CCORD2 = line2.split('\t')[2];
	GENE = line2.split('\t')[3];
	CCHROMlist.append(CCHROM)
	#these guys have to be integers or they won't work later
	CCORD1list.append(int(CCORD1))
	print CCORD1list
	CCORD2list.append(int(CCORD2))
	GENElist.append(GENE) 



#Here we go, we're running the position through the CORDlist range file. Now we just need a way to determine which number it is and the other guys that go with it.
num = 0
for item in POSlist:
#---------------------THIS IS THE PART THAT'S MESSED UP!!!!!!!!!!!!!!!!!!!!!!-------------------------(just letting you know), the problem is that we need integers to compare POSlist and CCORD1/CCORD2list and right now they're not integers.
	if POSlist[item] >= CCORD1list[num] and POSlist[item] <= CCORD2list[num]:
		print num
		#it isn't working, but if it did then I would do something like this
		line1 = CHROMlist[num] + '\t' + POSlist[num] + '\t' + IDlist[num] + '\t' + REFlist[num] + '\t' + VARlist[num] + '\t' + GENElist[num] + '\n'
		outfile.write(line1)
	#because there's 40 lines, if num is greater than 40 then we've scanned all of the lines in the output.txt file
	elif num > 39:
		index= POSlist.index(item)	
		line1 = CHROMlist[index] + '\t' + POSlist[index] + '\t' + IDlist[index] + '\t' + REFlist[index] + '\t' + VARlist[index] + '\tNone\n'
	else:
		num += 1



















