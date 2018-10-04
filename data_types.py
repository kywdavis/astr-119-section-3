import numpy as np

#integers

i = 10 # i is declared as an integer
print(type(i)) # type() returns the data type of the argument

a_i = np.zeros(i, dtype=int) #declare an array of ints length i, default dtype is float
print(type(a_i)) #will return ndarray
print(type(a_i[0])) #will return int64
print(a_i[0]) #should return 0

#floats

x = 119.0 # define x as a floating point number
print(type(x)) #will return float

y = 1.19e2 # float 119 in scientific notation
print(type(y)) # will return float

z = np.zeros(i,dtype=float) #declare array of floats
print(type(z)) #will return nd array
print(type(z[0])) # will return float 64
print (z[0])