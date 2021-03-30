import pandas as pd
iris = pd.read_csv('iris.csv')
a = iris['Species'].value_counts() # Counts the category
print(a)