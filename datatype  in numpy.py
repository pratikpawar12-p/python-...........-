# data type ---!!"
## int---!
import numpy as np
var = np.array([1,2,3,4])
print("data type" , var.dtype)

#flot----!!
var = np.array([1.3,2.3,3.9,4.7])
print("data type" , var.dtype)

#string---!!!
var = np.array(["a","b","c"])
print("data type" , var.dtype)

#string+int
var = np.array(["a","b","c",1,2,3,4])
print("data type" , var.dtype)

#change a data type---!!
x = np.array([1,2,3,4])
print("data type",x.dtype)

# changing data type this ---!!
x = np.array([1,2,3,4],dtype=np.int8)
print("data type",x.dtype)

#change a folt---!!
x = np.array([1,2,3,4],dtype="f")
print("data type",x.dtype)
print(x)



