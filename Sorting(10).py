# Exercise Intro to Tutorial Challenges

def introTutorial(V, arr):
    return arr.index(V)

# Exercise Insertion Sort - Part 1

def insertionSort1(n, arr):
    s = arr[n-1]
    sub = False
    for _ in range(2, n+1):
        if arr[-_] > s and _ < n +1:
            arr[-_ + 1] = arr[-_]
            sub = False
            print(*arr)
        elif arr[-_] <= s:
            arr[-_ + 1] = s
            sub = True
            print(*arr)
            break
    if sub == False:
        arr[0] = s
        print(*arr)

# Exercise Insertion Sort - Part 2

def insertionSort2(n, arr):
    for i in range(1, n):
        g = arr[i]
        j = i - 1
        while j >= 0 and g < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = g
        print(*arr)

# Exercise Quicksort 1 - Partition

def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = [p]
    for _ in range(1, n):
        if arr[_] < p:
            left.append(arr[_])
        elif arr[_] == p:
            equal.append(arr[_])
        elif arr[_] > p:
            right.append(arr[_])
    res = left + equal + right

    return res

# Exercise Quicksort 2 - Sorting

n = int(input())
ar = list(map(int, input().split()))


def quickSort(ar):
    if ar != []:
        p = ar[0]
        left = []
        right = []
        equal = [p]
        for _ in range(1, len(ar)):
            if ar[_] < p:
                left.append(ar[_])
            elif ar[_] == p:
                equal.append(ar[_])
            elif ar[_] > p:
                right.append(ar[_])
        res = quickSort(left) + equal + quickSort(right)
        if len(res) > 1:
            print(*res)
        return res
    else:
        return []


quickSort(ar)

# Exercise Counting Sort 1

def countingSort(arr):
    result = []
    for i in range(100):
        result.append(arr.count(i))
    return result

# Exercise Counting Sort 2

def countingSort(arr):
    result = []
    for i in range(100):
        result.append(arr.count(i))
    l = []
    for _ in range(len(result)):
        if result[_] > 0:
            for i in range(result[_]):
                l.append(_)
    return l

# Exercise Find the median

def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high


def findMedian(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    findMedian(arr, start, p - 1)
    findMedian(arr, p + 1, end)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    findMedian(arr, 0, len(arr) - 1)

    result = arr[int(len(arr) / 2)]

    fptr.write(str(result) + '\n')

    fptr.close()

# Exercise Correctness and the Loop Invariant

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))

# Exercise Running Time

def runningTime(arr):
    count = 0
    for i in range(1, n):
        g = arr[i]
        j = i - 1
        while j >= 0 and g < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            count += 1
        arr[j+1] = g
    return count