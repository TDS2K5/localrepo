from array import *

def ins(a,n):
    for i in range(n):
        v=a[i]
        j=i-1

        while j>=0 and a[j]>v:
            a[j+1]=a[j]
            j-=1
        a[j+1]=v

    return a

n=int(input("enter no of elements: "))
a=array('i',[])
for i in range(n):
    a.append(int(input(f"enter array element {i}")))

print(f"array before sorting: {a}")
print(f"array after sorting: {ins(a,n)}")