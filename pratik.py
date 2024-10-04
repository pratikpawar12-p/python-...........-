import numpy as np
my_array1=np.array(["ram",123,50.5,7+2j])
print(my_array1)
type(my_array1)
import numpy as np

# 1 d array 

print('1D array')
a = np.array([1,2,3,4,5])
print(a)

#2D array
print('2D array')
ar2 = np.array([[1,3,4,5],[1,3,4,4,]])
print(ar2)
#3D arrray 
print ('3D array')
c = np.array([[[1,4,5],[1,2,3],[3,4,5]]])
print(c)
   
print(a.size)

print(c.dtype)

x = [1,2,3,4,56,7,87]
y = np.array(x)
print(y)
print(type(y))
## how to creat array 
l = []
for i in range (1,5):
    int_1 = input("enter")
    l.append(int_1)
print(np.array(l))   

#with out string 
l = []
for i in range (1,5):
    int_1 = int(input("enter"))
    l.append(int_1)
print(np.array(l))   



 