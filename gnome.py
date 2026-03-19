import random

def gnome_sort(arr):
    comp = 0
    swaps = 0
    i = 0
    n = len(arr)

    while i < n:
        if i == 0:
            i += 1
            continue      
        comp += 1
        if arr[i] <= arr[i-1]:
            i += 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            swaps += 1
            i -= 1
    return comp, swaps

def random_list(size, min_val=0, max_val=10**6):
    return [random.randint(min_val, max_val) for _ in range(size)]

sizes = [1, 2, 3, 4, 5, 10, 250, 999, 9999]
print("Size\tComparisons\tSwaps")
for size in sizes:
    arr = random_list(size)
    comp, swaps = gnome_sort(arr)
    print(f"{size}\t{comp}\t\t{swaps}")