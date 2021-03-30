# Program to initialize array with random numbers
import numpy as np
n1 = np.random.randint(1,100,5) # (1,100,5) means within 1 to 100, we are extracting 5 random numbers
print(n1)
n2 = np.random.randint(100,1000,10) # (100,1000,10) means within 100 to 1000, we are extracting 10 random numbers
print(n2)