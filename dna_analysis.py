def count_freq(dna):
	codons = [dna[i:i+3] for i in range(0, len(dna),3 )]
	print "codons = " + str(codons)
	countA0 = 0
	countA1 = 0
	countA2 = 0
	countT0 = 0
	countT1 = 0
	countT2 = 0
	countG0 = 0
	countG1 = 0
	countG2 = 0
	countC0 = 0
	countC1 = 0
	countC2 = 0
	for i in codons:
		split = [codons[j:] for j in range(0, 3, 1)]
		if split[0]=='A' :
			countA0 +=1
		elif split[0]=='T' :
			countT0 +=1
		elif split[0]=='C' :
			countC0+=1
		elif split[0]=='G' :
			countG0+=1
		if split[1]=='A' :
			countA1 +=1
		elif split[1]=='T' :
			countT1 +=1
		elif split[1]=='C' :
			countC1+=1
		elif split[1]=='G' :
			countG0+=1
		if split[2]=='A' :
			countA2 +=1
		elif split[2]=='T' :
			countT2 +=1
		elif split[2]=='C' :
			countC2+=1
		elif split[2]=='G' :
			countG2+=1
	print """
				* base * 0 * 1 * 2 *
				********************  
				* A    * %d * %d * %d *
				* T    * %d * %d * %d *
				* G    * %d * %d * %d *
				* C    * %d * %d * %d *
				********************
				""" % (countA0,countA1,countA2,countT0,countT1,countT2,countG0,countG1,countG2,countC0,countC1,countC2) 
count_freq('ATGCAT')
