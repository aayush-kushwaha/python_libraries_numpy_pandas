import pandas as pd
iris = pd.read_csv('iris.csv')
a = iris.mean() #Prints mean
b = iris.median() #Prints median
c = iris.min() #Prints minimum
d = iris.max()#Prints maximum
print(a)
print(b)
print(c)
print(d)