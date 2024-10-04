import numpy as np
# insrt ---!!!
ar = np.array([1,1,1,2,3,4,5,6,7,8])

print(ar)
v =np.insert(ar,2,40)
print(v)

v =np.insert(ar,(2,4),40)
print(v)

# 2 --d arry---!!!!
print('2D array')
ar2 = np.array([[1,3,4,5],[1,3,4,4,]])
v1 = np.insert(ar2,2,6,axis=1)
print(v1)


# delete 
ar = np.array([1,1,1,2,3,4,5,6,7,8])

print(ar)
d =np.delete(ar,2)
print(d)


