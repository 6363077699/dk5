import numpy as np
arr=np.array(([2,3,4,],[1,6,5]))
print ("sum of the array=",arr.sum())
print("maximum of the array is=",arr.max())
print("minimum of the array is=",arr.min())
print("average of the array is=",np.average(arr))
print("arr.minimum of the array is=",arr.min(axis=1))
print("arr.maximum of the array is=",arr.max(axis=1))
print("arr.cumsum array is=",arr.cumsum(axis=1))

b=np.array([[3,6,9],[7,8,4]])
print("after adding matrisies is:",arr+b)
print("after multipling matrisies is:",arr*b)
print("after div matrisies is:",arr/b)
print("after substraction matrisies is:",arr-b)


