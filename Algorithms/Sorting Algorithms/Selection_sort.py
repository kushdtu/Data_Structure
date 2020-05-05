from typing import List

def findMinIndex(A: List[int], start: int):
    minIndex = start
    start += 1
    while start < len(A):
        if A[start] < A[minIndex]:
            minIndex = start
        start += 1
    return minIndex

def selectionSort(arr: List[int]):
    i = 0
    while i < len(arr):
        minIndex = findMinIndex(arr, i)
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        i += 1

arr = [25, 17, 31, 13, 2]
selectionSort(arr)
print(arr)