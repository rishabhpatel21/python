# DSA Question 2 : Find Min and Max of Array
# function to short array and then getting the 1st and last index number as min max
def getminmax(arr):
    arr.sort()# shorts array in number order
    minmax = {"min":arr[0] , "max":arr[-1]} # dic to store min and mix values of array.
    return minmax

if __name__ == "__main__":
    arr = [100,20,3,43,15]
    minmax = getminmax(arr)
    print("minimum value:", minmax["min"]) # prints minimum  value of array
    print("maximum value:", minmax["max"]) # prints mximum value of array