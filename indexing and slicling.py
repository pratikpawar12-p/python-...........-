import numpy as np
## indexing ---!!!
# 1-d array----
ar = np.array([9,0,4.5])
#              0,1,2,3.....! posstive indexing
# negtive indexing .......-4,-3,-2,-1
print(ar[1])
print(ar[-3])

# 2-d array----
ar1 = np.array([[1,2,3],[4,5,6]])
print(ar1)
print(ar1[0,2])


# 3 -d array----

var = np.array([[[1,3],[6,8]]])
print(var[0,1,1])



## 2 = slicing-------!!!!
ar = np.array([9,0,4.5,8,10,22])
#              0,1,2,3.....! posstive indexing
# negtive indexing .......-4,-3,-2,-1
print( "o to 8 data :--", ar[1:4])
print( "o to end :--", ar[1:])
print( "start to 8 :--", ar[:4])
print("stop :--",ar[::])
print("stop :--",ar[::3])
print("stop :--",ar[1:3:2])

# 2-d array----
ar1 = np.array([[1,2,3],[4,5,6],[3.4,6,5]])
print(ar1)
print( " 4 to 6 tak data :--",ar1[1,0:])


# 3 -d array----

var = np.array([[[1,3],[6,8]]])
print(var[0,1,1])
