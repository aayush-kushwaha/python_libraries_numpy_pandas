import pandas as pd
iris = pd.read_csv('iris.csv')
def half(n):
    return n * 0.5
a = iris[['Sepal.Length','Petal.Length']].apply(half)
print(a)

def double(n):
    return n * 2
b = iris[['Sepal.Length','Petal.Length']].apply(double)
print(b)