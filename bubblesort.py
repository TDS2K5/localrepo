arr=[]
n=int(input("enter array size: "))
for s in range(n):
    ai=int(input(f"enter element {s}: "))
    arr.append(ai)
print(arr)

n=len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)





