#airthmetic operation 2....!!

#np.min()
#===
#np.max()
import numpy as np
ar = np.array([1.34,7,45,544,4,])
print('max value =:', np.max(ar))
print('min value = :', np.min(ar))


#np.argmin() &  np.argmax() = index value.....--!
ar = np.array([1.34,7,45,544,4,])
print('max value =:', np.argmin(ar))
print('min value = :', np.argmax(ar))


# 2 - D 
var = np.array([[12,3,4,5],[1,34,5,6]])
print('max value =:', np.max(var,axis=1))
print('min value = :', np.min(var,axis=0))

#np.sqrt()
var = np.array([[12,3,4,5],[1,34,5,6]])

print('squre rooot =' , np.sqrt(var))
#np.sin()
var = np.array([[12,3,4,5],[1,34,5,6]])
print('sin value=',np.sin(var))
#np.cos()
var = np.array([[12,3,4,5],[1,34,5,6]])
print('cos value=',np.cos(var))
#np.cumsum() # add the pariviose value step by step
var = np.array([[12,3,4,5],[1,34,5,6]])
print('cumsum=',np.cumsum(var))

