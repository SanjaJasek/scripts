#!/usr/bin/env python

#DNASeq = 'ATGAAC'
DNASeq = raw_input("Enter a DNA sequence:\n")
DNASeq = DNASeq.upper()

#print 'Sequence', DNASeq # -> only python 2
print ('Sequence ' + DNASeq ) # -> python 2 and 3

SeqLength = float(len(DNASeq))
print( 'Length is ' + str(SeqLength))


NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')

print('A: {:.2f}'.format(NumberA / SeqLength))
print('T: {:.2f}'.format(NumberA / SeqLength))
print('G: {:.2f}'.format(NumberA / SeqLength))
print('C: {:.2f}'.format(NumberA / SeqLength))

TotalStrong = NumberC + NumberG
TotalWeak = NumberA + NumberT


if SeqLength <=14:
	MeltTemp = ( 4 * TotalStrong ) + ( 2 * TotalWeak )
	print("Using short formula.")
else:
	MeltTemp = 64.9 + 42 * (TotalStrong - 16.4) / SeqLength
	print("Using short formula.")

print( "Melting Temp: {}".format(MeltTemp))