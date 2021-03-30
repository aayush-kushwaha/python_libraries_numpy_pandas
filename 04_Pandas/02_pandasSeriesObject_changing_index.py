# By default the place of index starts from 0,1,2,3,4.........
# To change the format of 0,1,2,3,4... to a,b,c,d,e below code is written
import pandas as pd
s1 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1)