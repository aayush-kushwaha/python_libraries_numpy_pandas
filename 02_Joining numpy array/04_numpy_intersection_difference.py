import numpy as np
n1 = np.array([10,20,30,40,50,60])
n2 = np.array([50,60,70,80,90])

print(np.intersect1d(n1,n2)) # Prints only common element of n1 and n2

print(np.setdiff1d(n1,n2))   # subtracts n2 from n1 and prints the value of n1

print(np.setdiff1d(n2,n1))   # subtracts n1 from n2 and prints the value of n2

