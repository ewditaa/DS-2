import random
import time

# --------------------------
# INSERTION SORT
# --------------------------
def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# --------------------------
# MERGE SORT
# --------------------------

def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# --------------------------
# QUICK SORT
# --------------------------

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# --------------------------
# TIME MEASUREMENT
# --------------------------

def measure_time(sort_func, arr):

    data = arr.copy()

    start = time.time()

    if sort_func == quick_sort:
        sort_func(data, 0, len(data) - 1)
    else:
        result = sort_func(data)
        if result is not None:
            data = result

    end = time.time()

    return end - start


# --------------------------
# DATASET GENERATOR
# --------------------------

def generate_datasets(size):

    random_list = [random.randint(1, 100000) for _ in range(size)]

    sorted_list = list(range(size))

    reverse_list = list(range(size, 0, -1))

    return random_list, sorted_list, reverse_list


# --------------------------
# MAIN PROGRAM
# --------------------------

if __name__ == "__main__":

    print("Correctness Check")

    test = [5, 2, 9, 1, 5, 6]

    arr1 = test.copy()
    insertion_sort(arr1)

    arr2 = merge_sort(test.copy())

    arr3 = test.copy()
    quick_sort(arr3, 0, len(arr3) - 1)

    print("Insertion:", arr1)
    print("Merge:", arr2)
    print("Quick:", arr3)

    sizes = [1000, 5000, 10000]

    print("\nPerformance Results")

    for size in sizes:

        random_list, sorted_list, reverse_list = generate_datasets(size)

        print(f"\nDataset Size: {size}")

        print("Random Data")
        print("Insertion:", measure_time(insertion_sort, random_list))
        print("Merge:", measure_time(merge_sort, random_list))
        print("Quick:", measure_time(quick_sort, random_list))

        print("Sorted Data")
        print("Insertion:", measure_time(insertion_sort, sorted_list))
        print("Merge:", measure_time(merge_sort, sorted_list))
        print("Quick:", measure_time(quick_sort, sorted_list))

        print("Reverse Data")
        print("Insertion:", measure_time(insertion_sort, reverse_list))
        print("Merge:", measure_time(merge_sort, reverse_list))
        print("Quick:", measure_time(quick_sort, reverse_list))