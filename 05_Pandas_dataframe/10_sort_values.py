import pandas as pd
iris = pd.read_csv('iris.csv')
a = iris.sort_values(by='Sepal.Length') # Sorts the Sepal.Length row into ascending order
print(a)