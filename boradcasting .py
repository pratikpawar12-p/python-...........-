#--- error !!
#import numpy as np 
#var1 = np.array([1,3,4,5])
#var2 = np.array([1,3,4])
#print (var1 + var2)

#ValueError: operands could not be broadcast together with shapes (4,) (3,)
 #rule---1 = same dimension
import numpy as np 
var1 = np.array([1,3,4,5])
var2 = np.array([1,3,4,5])
print (var1 + var2)

#rule no 2----
var1 = np.array([1,3,4,5])
print(var1.shape)
var2 =np.array([[1],[3],[5]])
print(var2.shape)