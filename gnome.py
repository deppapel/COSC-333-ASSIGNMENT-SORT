# desc
def gnome_sort(arr):
    comp = 0
    swaps = 0
    i = 0
    n = len(arr)

    while i < n:
        if i == 0:
            i+=1
            comp += 1
        if arr[i] <= arr[i-1]:
            i+=1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i] 
            swaps += 1      
            i-= 1   
    return comp, swaps

numbers_input = input("Enter integers separated by spaces: ")
lists = list(map(int, numbers_input.split()))
comp, swaps =gnome_sort(lists)

print("sorted is :", lists)
print("comparisons are:", comp)
print("swaps are :", swaps)