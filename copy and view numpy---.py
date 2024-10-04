#copy vs view 

import numpy as np
var = np.array([2,3,4,589,7]) 

# copy _----!!!
co = var.copy()

print ("var = ", var)
print("copy = " , co)


# view 
x = np.array([1,3,3,4,5,6])
vi = x.view ()
print ("x =",x)
print("view=",vi)