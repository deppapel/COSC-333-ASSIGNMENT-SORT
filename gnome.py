# desc
def gnome_sort(arr):
   
    i = 0
    n = len(arr)

    while i < n:
        if i == 0:
            i+=1
        if arr[i] <= arr[i-1]:
            i+=1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]       
            i-= 1
       
lists = [5, 1, 4, 2, 3]
gnome_sort(lists)
print("sorted is :", lists)