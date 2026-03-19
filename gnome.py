import random

def gnome_sort(arr, verbose=False):
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
            if verbose:
                print(f" Swap {swaps}: {arr}")
    return comp, swaps

def random_list(size, min_val=0, max_val=10**6):
    return [random.randint(min_val, max_val) for _ in range(size)]



sizes = [1, 2, 3, 4, 5, 10, 250, 999, 9999]
print("Size\tOriginal (first 5)\tSorted (first 5)\tComparisons\tSwaps")
for size in sizes:
    arr = random_list(size)
    original = arr.copy()
    comp, swaps = gnome_sort(arr)

    orig_preview = str(original[:5])[:-1] + ",...]" if size > 5 else str(original)
    sort_preview = str(arr[:5])[:-1] + ",...]" if size > 5 else str(arr)

    print(f"{size}\t{orig_preview}\t{sort_preview}\t{comp}\t{swaps}")