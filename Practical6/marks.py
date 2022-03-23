marks=[45,36,86,57,53,92,65,45]
marks.sort()
print (marks)

import matplotlib.pyplot as plt
import numpy as np
x=np.array(marks)
a = np.quantile(marks,0.75)
b = np.quantile(marks,0.25)
up = a + 1.5*(a-b)
down = b - 1.5*(a-b)
shangjie = x[x < up][-1]
xiajie = x[x > down][0]
plt.grid(True)
y = plt.boxplot(x, meanline=True, showmeans=True)
plt.show()
