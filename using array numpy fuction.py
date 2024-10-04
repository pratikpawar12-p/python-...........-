# create numpy arra usning numpy functions
# #  zeros .....function 
import numpy as np
ar_zero = np.zeros(4)
print(ar_zero)

# multiple dimanational 
ar_zero1 = np.zeros((3,3))
print(ar_zero1)


## ones.....function

ar_ones = np.ones(4)
print(ar_ones)

### empty......function

ar_em = np.empty(7)
print(ar_em)


#### range......!! arange function 
ar_rn = np.arange(4)
print(ar_rn)


##### digonal .......!! eye function
ar_dia = np.eye(3)
print(ar_dia)
print( )
ar_dia = np.eye(3,4)
print(ar_dia)


###### linespace

ar_line = np.linspace(1,20 , num=3)
print(ar_line)