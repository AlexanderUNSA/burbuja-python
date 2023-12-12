import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

sizes = [100, 1000, 2000, 3000, 4000, 5000]

for size in sizes:
    # Generate a random list
    lst = [random.randint(0, 1000) for _ in range(size)]

    # Measure the time taken to sort
    start_time = time.time()
    bubble_sort(lst)
    elapsed_time = time.time() - start_time

    print(f"Size: {size}, Time: {elapsed_time:.6f} seconds")

