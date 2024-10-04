
# Arithmetic function----
import numpy as np
# shuffle
ar = np.array([1,1,1,2,3,4,5,6,7,8])
np.random.shuffle(ar) 
print(ar)

# unique 
ar = np.array([1,1,1,2,3,4,5,6,7,8])
x=np.unique(ar) 
print(x)
# index number---
ar = np.array([1,1,1,2,3,4,5,6,7,8])
x=np.unique(ar,return_index=True) 
print(x)
# count ----
ar = np.array([1,1,1,2,3,4,5,6,7,8])
x=np.unique(ar,return_counts=True) 
print(x)
# resize 
ar = np.array([1,1,1,2,3,4,5,6,7,8])
y=np.resize(ar,(4,3)) 
print(y)

# flatten
ar = np.array([1,1,1,2,3,4,5,6,7,8])
y=np.resize(ar,(4,3)) 
print("flatten:=",y.flatten())
print("revel=",y.ravel())
# ravel 
