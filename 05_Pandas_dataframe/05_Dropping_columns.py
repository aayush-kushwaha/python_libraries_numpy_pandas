import pandas as pd
iris = pd.read_csv('iris.csv')
a = iris.drop("Sepal.Length",axis = 1)#axis = 1 means column 
print(a)