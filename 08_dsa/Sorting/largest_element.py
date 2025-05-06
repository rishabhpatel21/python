def largest_element(arr):
    arr.sort()
    largest_element = arr[-1]
    return largest_element
    

def largest_element_method2(arr):
    largest_element = arr[0]
    for i in arr:
        if i > largest_element:
            largest_element = i
    return largest_element

if __name__ == "__main__":
    arr = [1,4,3,7,5,2,6]
    print(largest_element_method2(arr))