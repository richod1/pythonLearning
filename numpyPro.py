import numpy as np

arr=np.array([[1,2,3,4,5],[2,4,6,8,10]])
print(arr[0][3])

#3D array
arr1=np.array([[[1,2,3,4,5],[2,4,6,8,10],[1,3,6,9,13]]])
print(arr1)

arra2=np.array([1,2,3,4],ndmin=5)
print(arra2)
print("number of array dimention :",arra2.ndim)