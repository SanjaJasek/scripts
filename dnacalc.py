#!/usr/bin/env python

DNASeq = 'ATGAAC'

#print 'Sequence', DNASeq # -> only python 2
print ('Sequence ' + DNASeq ) # -> python 2 and 3

SeqLength = float(len(DNASeq))
print( 'Length is ' + str(SeqLength))


NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')

print('A: ' + str( NumberA / SeqLength * 100 ) +'%')
print('T: ' + str( NumberT / SeqLength * 100 ) +'%')
print('G: ' + str( NumberG / SeqLength * 100 ) +'%')
print('C: ' + str( NumberC / SeqLength * 100 ) +'%')