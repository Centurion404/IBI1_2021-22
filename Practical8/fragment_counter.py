seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
import re
pos = re.findall(r'GAATTC',seq)
L = len(pos)
print (L+1)
