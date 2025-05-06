arr = [ 1,2,1,4,3,2,5]
print("Array is: ",arr)
num = int(input("Enter the number to check duplicates: "))

def countdup(num ,arr):
    count= 0
    n = len(arr)
    for i in range(0 ,n-1):
        if num != arr[i]:
            continue
        if arr[i] == num:
            count += 1
    return count    
    
print("Number of duplicates are: ",countdup(num ,arr))