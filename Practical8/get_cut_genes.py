seq1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
seq = seq1.read()
import re
pos = re.findall(r'GAATTC.*?>',seq)
print (pos)
