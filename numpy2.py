from numpy import *

arr1=array([1,2,3,4,5])
#Now i want to add the 5 in each element
arr1=arr1+5 #it will add the value 5 in each value
print(arr1)
arr2=array([6,3,3,2,1])
arr3=arr1+arr2 #it is also called vectorization
print(arr3)
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
print(concatenate([arr1,arr2]))


#copy of the array
arr2=arr1 #this is also called the aliasing
print(arr2)
print(arr1)
print(id(arr1))
print(id(arr2))
#now if we want to create really a different array by copying it or we can say that both arrays should contain the different address
arr2=arr1.view()
#Now if we change the value of arr1 then unfortunately same changes would be reflect into the arr2
#like
arr1[1]=9 #this is something which we dont want this is called the shallow copy
print(arr1)
print(arr2)
#so  we can say shallow copy is the copy in which if we change in the first one then same changes would we reflect into the anoter
print(id(arr1))
print(id(arr2))
#But how to achieve which we want that can be done by using the function copy() which creates the deep copy
arr2=arr1.copy()
arr1[2]=10
arr2[3]=40 #for deep copy we use the function .copy() for shallow copy we use the method .view()
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)
#so deep copy is the copy which creates the two different array in real manner changes in one copy does not reflect into another it will create two different copy which are not linked with each other























