import numpy
arr=numpy.array([1,2,3])
print(arr)
print(arr.dtype) #this is to check the datatype of the array

arr1=numpy.array([1,2,3,4.0],int)#here we are providing the datatype also
print(arr1.dtype) #this is to check the datatype of the array
print(arr1)

print
print

arr2=numpy.linspace(0,15,20) #here basically the 16 will break the range(0,15) into 20 different parts if we don't mention the 20  here then by default it will break the all the values into 50 parts
print(arr2)

arr3=numpy.arange(1,15,2) #here 2 is the steps or number of jumps between 1to 15
print(arr3)


arr4=numpy.logspace(1,40,1) # here the 5 is the total no. of elements in the array and 40 will divide as 10^1 10^10 10^20 10^30 10^40
print(arr4)
print('%.2f'%arr4[0])

arr5=numpy.zeros(5)

print(arr5)


arr6=numpy.ones(5)
print(arr6)
