##--- for loop use
import numpy as np 
ar = np.array([9,0,4.5]) 
print(ar)
print( )
for i in ar:
    print(i)


# 2-d array---- 2 time's for
ar1 = np.array([[1,2,3],[4,5,6]])
print(ar1)
for i in ar1:
    print(i)

## value Iterating ---!!
ar1 = np.array([[1,2,3],[4,5,6]])
print(ar1)
for i in ar1:
    print(i)
for k in ar1:
    print(k)
    for l in k:
        print(l)

# 3 -d array----3 time for loop 

ar1 = np.array([[[1,3,4],[6,8,4]]])
print(ar1)
for i in ar1:
    print(i)
for k in ar1:
    print(k)
    for l in k:
        print(l)
        for j in l:
            print(j)

## nditen ()
ar1 = np.array([[[1,3,4],[6,8,4]]])
print(ar1)

for i in np.nditer(ar1):
    print(i)

# data type change----
ar1 = np.array([[[1,3,4],[6,8,4]]])
print(ar1)

for k in np.nditer(ar1,flags=['buffered'],op_dtypes=["S"]):#chnage a data type 
    print(k)


# indexing ke sath Iterating - - ndenumerate ()

ar1 = np.array([[[1,3,4],[6,8,4]]])
print(ar1)


for i,d in np.ndenumerate(ar1):
    print(i)



            