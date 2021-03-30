import pandas as pd
iris = pd.read_csv('iris.csv')
a = iris.drop([1,2,3],axis=0)
print(a)