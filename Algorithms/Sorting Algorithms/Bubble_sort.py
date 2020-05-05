from typing import List

def bubbleSort(arr: List[int]):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return

arr = [25, 17, 31, 13, 2]
bubbleSort(arr)
print(arr)