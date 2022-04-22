import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("c:\\Users\\Colorful\\IBI1_2021-22\\Practical7")
covid_data = pd.read_csv("full_data(2).csv")
covid_data.head(5)
covid_data.info()
covid_data.describe()
print (covid_data.iloc[10:21,0])
print (covid_data.iloc[10:21,2])
print (covid_data.loc[1454:1545,'new_cases'].quantile(0.5))
print (covid_data.loc[1454:1545,'new_deaths'].quantile(0.5))
 #boxplot

 #boxplot
plt.plot (covid_data.loc[1454:1545,'date'],covid_data.loc[1454:1545,'new_cases'],'b+')
plt.show()
