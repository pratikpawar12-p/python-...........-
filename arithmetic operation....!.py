# airthmetic operation ....!!
# 1 - D array -----!!!
#a+b or np.add(a,b)
import numpy as np 
var = np.array([1,2,35,67,75])
varadd = var + 2
print(varadd)

# &
var1 = np.array([1,2,35,67,75])
var2 = np.array([2,5,6,8,8])
varadd = var1 + var2
print(varadd)


#a-b or np.subtract(a,b)
import numpy as np 
var = np.array([1,2,35,67,75])
sub = var - 2
print(sub)

# &
var1 = np.array([1,2,35,67,75])
var2 = np.array([2,5,6,8,8])
varsub = var1 - var2
print(varsub)


#a*b or np.multiply(a,b)
import numpy as np 
var = np.array([1,2,35,67,75])
mul = var * 2
print(mul)

# &
var1 = np.array([1,2,35,67,75])
var2 = np.array([2,5,6,8,8])
varmul = var1 * var2
print(varmul)
#a/b or np.divide(a,b)
#a%b or np.mod(a,b)
#a**b or np.power(a,b)
#1/a  or np.reciprocal(a)

# 2nd ----::

import numpy as np 
var = np.array([2,35,67,75])
sub = np.subtract(var,3)
print(sub)

# &
var1 = np.array([1,2,35,67,75])
var2 = np.array([2,5,6,8,8])
varsub = np.subtract(var1,var2)
print(varsub)




# 2-D array ----!!!!


var1 = np.array([[1,2,35,67,75],[1,33,5,5,6]])
var2 = np.array([[2,5,6,8,8],[1,23,3,4,34]])

add = var1 + var2
print(add)