def sort(arr):
    n=len(arr)
    i = 0

    for i in range(i,n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr


arr = [ 13,46,24,40,20,9 ]
print("Array is: ",arr)
print("Sorted array is: ",sort(arr)) 
