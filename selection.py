# Go through the array to find the lowest value.
# Move the lowest value to the front of the unsorted part of the array.
# Go through the array again as many times as there are values in the array.

arr=[]
n=int(input("enter array size: "))
for s in range(n):
    ai=int(input(f"enter element {s}: "))
    arr.append(ai)
print(arr)

