lp=[30,35,40,45,50,55,60,65,70,75]
lc=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
dic={}
for m, n in zip(lp,lc):
	dic[m] = n
print (dic)

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (10,10), dpi=100)
plt.scatter(lp,lc)
plt.show()

h=40
i=dic[h]
print (i)
