from array import *

def minmax(arr, low, high):
    # base case: only one element
    if low == high:
        return arr[low], arr[low]

    # base case: only two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # divide
    mid = (low + high) // 2

    # conquer
    mini1, maxi1 = minmax(arr, low, mid)
    mini2, maxi2 = minmax(arr, mid+1, high)

    # combine
    return min(mini1, mini2), max(maxi1, maxi2)


# driver
n = int(input("enter no of elements: "))
arr = array('i', [])
for i in range(n):
    arr.append(int(input(f"enter array element {i}: ")))

print(f"array: {arr}")
mini, maxi = minmax(arr, 0, n-1)
print("minimum value:", mini)
print("maximum value:", maxi)
