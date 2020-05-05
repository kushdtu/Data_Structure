
def findAvg(k, arr):
    result = []

    windowStart = 0
    windowSum = 0.0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            result.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1

    return result

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(findAvg(5, arr))
