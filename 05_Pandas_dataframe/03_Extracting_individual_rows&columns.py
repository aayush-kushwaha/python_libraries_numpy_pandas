import pandas as pd
iris = pd.read_csv('iris.csv')
a = iris.iloc[0:3,0:2]
print(a)