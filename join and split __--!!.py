## join--- concatenate()
# 1 - D array ---!!
import numpy as np
ar1 = np.array([1,3,4])
ar2=  np.array([4,5,7])
ar= np.concatenate((ar1,ar2))
print(ar)

# 2 - D array---!!
ar1 = np.array([[1,2,3],[4,5,6]])
ar2 = np.array([[1,2,3],[4,5,6]])
ar= np.concatenate((ar1,ar2),axis=1)
print(ar)

# axis =0
ar1 = np.array([[1,2,3]])
ar2 = np.array([[1,2,3]])
ar= np.concatenate((ar1,ar2),axis=0)
print(ar)
# and ----
# stack ()----!!!
ar1 = np.array([[1,2,3]])
ar2 = np.array([[4,5,6]])
ar= np.stack((ar1,ar2))
print(ar)

# h ---- row 
ar1 = np.array([[1,2,3]])
ar2 = np.array([[4,5,6]])
ar= np.hstack((ar1,ar2))
print(ar)

# d ----hight
ar1 = np.array([[1,2,3],[4,5,6]])
ar2 = np.array([[1,2,3],[4,5,6]])
ar= np.dstack((ar1,ar2))
print(ar)

# v----colum 
ar1 = np.array([[1,2,3],[4,5,6]])
ar2 = np.array([[1,2,3],[4,5,6]])
ar= np.vstack((ar1,ar2))
print(ar)


# split ___!!

print("split ----------!!!")

ar = np.array([9,0,4.5,4,6,7,8])
print (ar)

ar = np.array_split(ar,3)
print(ar)

print(ar[1]) # single array 

#2 - d array----

ar1 = np.array([[1,2,3],[4,5,6],[1,3,2]])
ar = np.array_split(ar,2,axis=1)
print(ar)