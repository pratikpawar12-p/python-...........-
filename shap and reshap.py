#shap-------!!! 2D and 3D dimational me convart 

import numpy as np 
var = np.array([[12,3,4,5],[1,34,5,6]])
print(var)
print(var.shape)

var = np.array([12,3,4,5],ndmin=4  )
print(var)
print(var.ndim)
print(var.shape)


#re-shap 1 D se 2D
ar = np.array([1.34,7,45,544,4,5])
print(ar)
x = ar.reshape(3,2)
print(x)

# 2d se 3d
ar = np.array([1,7,45,544,4,54,5,7,6,3,4,5])
print(ar)
x = ar.reshape(2,3,2)
print(x)