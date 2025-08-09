# Go through the array to find the lowest value.
# Move the lowest value to the front of the unsorted part of the array.
# Go through the array again as many times as there are values in the array.

# arr=[]
# l=int(input("enter array size: "))
# for s in range(l):
#     ai=int(input(f"enter element {s}: "))
#     arr.append(ai)

# n=len(arr)

# for i in range(n-1):
#     mindex=i
#     for j in range(i+1,n):
#         if arr[j]<arr[mindex]:
#             mindex=j
    
#     arr[i],arr[mindex]=arr[mindex],arr[i]

# print(arr)

# using array
from array import *
def s(a,n):
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if a[j]<a[mini]:
                mini=j

        a[i],a[mini]=a[mini],a[i]
    return a

n=int(input("enter number of elements: "))
a=array("i",[])

for i in range(n):
    e=int(input(f"enter array element {i}: "))
    a.append(e)

print(f"before sorting: {a}")
print(f"after sorting: {s(a,n)}")





























