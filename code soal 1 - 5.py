import random
import time

# =========================
# SOAL 1
# Modified Binary Search
# =========================

def countOccurrences(arr, target):

    # cari posisi pertama
    left = 0
    right = len(arr) - 1
    first = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # cari posisi terakhir
    left = 0
    right = len(arr) - 1
    last = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if first == -1:
        return 0

    return last - first + 1


# =========================
# SOAL 2
# Bubble Sort Analisis
# =========================

def bubbleSort(arr):

    arr = arr.copy()
    n = len(arr)

    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1

        for j in range(0, n-i-1):
            comparisons += 1

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True

        print("Pass", passes, ":", arr)

        if not swapped:
            break

    return arr, comparisons, swaps, passes


# =========================
# SOAL 3
# Hybrid Sort
# =========================

def insertionSort(arr):

    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j+1] = arr[j]
            swaps += 1
            j -= 1

        arr[j+1] = key

    return arr, comparisons, swaps


def selectionSort(arr):

    comparisons = 0
    swaps = 0

    for i in range(len(arr)):

        min_idx = i

        for j in range(i+1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1

    return arr, comparisons, swaps


def hybridSort(arr, threshold=10):

    arr = arr.copy()

    if len(arr) < threshold:
        return insertionSort(arr)
    else:
        return selectionSort(arr)


# =========================
# SOAL 4
# Merge 3 Sorted Lists
# =========================

def mergeThreeSortedLists(A, B, C):

    i = j = k = 0
    result = []

    while i < len(A) or j < len(B) or k < len(C):

        a = A[i] if i < len(A) else float('inf')
        b = B[j] if j < len(B) else float('inf')
        c = C[k] if k < len(C) else float('inf')

        minimum = min(a, b, c)

        result.append(minimum)

        if minimum == a:
            i += 1
        elif minimum == b:
            j += 1
        else:
            k += 1

    return result


# =========================
# SOAL 5
# Inversion Counter
# =========================

def countInversionsNaive(arr):

    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


def merge(arr):

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, inv_left = merge(arr[:mid])
    right, inv_right = merge(arr[mid:])

    result = []
    i = j = 0
    inv = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv += len(left) - i
            j += 1

    result += left[i:]
    result += right[j:]

    return result, inv + inv_left + inv_right


def countInversionsSmart(arr):

    _, inv = merge(arr)
    return inv


# =========================
# TEST PROGRAM
# =========================

if __name__ == "__main__":

    print("=== SOAL 1 ===")
    arr = [1,2,4,4,4,7,9,12]
    print("Jumlah kemunculan 4:", countOccurrences(arr,4))


    print("\n=== SOAL 2 ===")
    print(bubbleSort([5,1,4,2,8]))


    print("\n=== SOAL 3 ===")
    data = [random.randint(1,100) for _ in range(10)]
    print("Data:",data)
    print("Hybrid Sort:", hybridSort(data))


    print("\n=== SOAL 4 ===")
    print(mergeThreeSortedLists(
        [1,5,9],
        [2,6,10],
        [3,4,7]
    ))


    print("\n=== SOAL 5 ===")
    arr = [3,1,2]

    print("Naive:", countInversionsNaive(arr))
    print("Smart:", countInversionsSmart(arr))