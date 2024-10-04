# function_-----numpy !!!----
import numpy as np
# search --- where()__!! # find the indexing value
ar = np.array([1,1,1,2,3,4,5,6,7,8])
x = np.where (ar==3) 
print(x)

# sort 
ar = np.array([1,1,1,2,3,4,5,6,7,8])
x = np.sort (ar) 
print(x)
# string sort ---!!!
ar = np.array(["pratik","pawar","shizuka","pawar"])
x = np.sort(ar)
print(x)
# 2-d array---- 
ar1 = np.array([[1,2,5],[4,3,6]])
x = np.sort(ar1)
print(ar1)
# search sort ----
ar = np.array([1,1,1,2,3,4,5,6,7,8])
x = np.searchsorted (ar,3) 
# 2 nd -----------method
x1 = np.searchsorted (ar,[3,4,5],side ="right") 
print(x1)
print(x)
# filter 
ar = np.array(["pratik","pawar","shizuka","pawar"])
f = [True,False,False,True]
ar1 = ar[f]
print(ar1)




# Arithmetic function----

# shuffle
ar = np.array([1,1,1,2,3,4,5,6,7,8])
x = np.random.shuffle(ar) 
print(x)

# unique 
# resize 
# flatten
# ravel 
