import pandas as pd
iris = pd.read_csv('iris.csv')
a = iris.loc[0:3,("Sepal.Length","Petal.Length")]
#Above in .loc in [0:3], 3 is inclusive. 0,1,2,3 index will be printe and this unlike list indexing method
print(a)