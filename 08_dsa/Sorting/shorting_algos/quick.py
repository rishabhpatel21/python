def sort(array):
    print(array)
    
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return sort(less) + [pivot] + sort(greater)


arr = [ 1,5,3,7,2,8,4,6 ]
print(sort(arr))