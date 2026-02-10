import numpy as np

'''
import pandas as pd

#print("NumPy version:", np.__version__)
#print("Pandas version:", pd.__version__)


a=np.array(45)
b=np.array([12,13,14])
c=np.array([[1,2,3],
            [4,5,6]])
result = a+b+c
print(result)
'''
'''arr=np.arange(12)
reshaped=arr.reshape(3,4)

print(reshaped)
a =np.array([[1,2]])
b =np.array([[3,4]])
vstacked=np.vstack((a,b))
hstacked=np.hstack((a,b))
print(vstacked,hstacked)'''


data =np.array([[10,20,30],[20,50,60]])
print(np.mean(data))

print(np.mean(data,axis=0))
