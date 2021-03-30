## hstack()
'''
Basically hstack() is used to horizontally stack two numpy arrays
For e.g.:
n1 = [10,20,30]
n2 = [40,50,60]
Output after using hstack:-
array([[10,20,30,40,50,60]])
'''
import numpy as np
n1 = np.array([10,20,30])
n2 = np.array([100,200,300])

print(np.hstack((n1,n2)))