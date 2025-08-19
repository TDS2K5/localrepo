from array import *

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        B=arr[:mid]
        C=arr[mid:]

        mergesort(B)
        mergesort(C)
        merge(B,C,arr)

    return arr

def merge(B,C,arr):
    i=j=k=0
    p=len(B)
    q=len(C)

    while i<p and j<q:
        if B[i]<C[j]:
            arr[k]=B[i]
            i+=1
        else:
            arr[k]=C[j]
            j+=1

        k=k+1

    while i<p:
        arr[k]=B[i]
        i+=1
        k+=1

    while j<q:
        arr[k]=C[j]
        j+=1
        k+=1

n=int(input("enter array size: "))
arr=array('i',[])

for i in range(n):
    arr.append(int(input(f"enter array element {i}: ")))

print(arr)
su=mergesort(arr)
print(su)




