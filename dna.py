def count_dna(dna, base):
	dna = list(dna)
	i = 0
	for c in dna:
		if (c == base):
			i=i+1
	return i
dna = raw_input(" Enter the DNA sequence ")
base = raw_input (" Enter the base whose number you wanna calculate ")
print "The aove DNA has " + str(count_dna(dna, base)) + str(base)
