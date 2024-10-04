#How to Create NumPy Arrays with Random Numbers ....!!

# rand = random value between 0 to 1 '''!!

import numpy as np
var = np.random.rand(4)
print(var)

var1 = np.random.rand(4,3)
print(var1)


## randn = close to zero and negtive - value 

var2 = np.random.randn(5)
print(var2)

var2 = np.random.randn(5,4)
print(var2)

### ranf() = shaps ans files with random floats in the open [0.0,1.0]...!!

var3 = np.random.ranf(4)
print(var3)

#### randint ---- min max 

var4 = np.random.randint(5,27,2)
print(var4)