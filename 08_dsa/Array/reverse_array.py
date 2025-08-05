# DSA Question 1 : Reverse an array.

#Without using reverse function
def reverseArray(arr1):
    n = len(arr1) # Here n = length of array

    temp = [0] * n  # It will create  temp array length of original array temp = [0,0,0,0,0]

    for i in range( n ): # range(0,5)
        temp[i] = arr1[n - i - 1]
        # [5, 0, 0, 0, 0]
        # [5, 4, 0, 0, 0]
        # [5, 4, 3, 0, 0]
        # [5, 4, 3, 2, 0]
        # [5, 4, 3, 2, 1]

    for i in range(n):
        arr1[i] = temp[i]
#By using reverse function
def reverseusingfunction(arr2):
    arr2.reverse()

# Initialising array values
if __name__ == "__main__":
    arr1 = [1,2,3,4,5]
    arr2 = [6,7,8,9,10]
    # Function call
    reverseArray(arr1)
    print("Without using reverse function: ")
    # It will run till length of arr1 and print each item one by one
    for i in range(len(arr1)):
        print(arr1[i] , end=  " ")

    # To add new line
    print("")
    print("")
    # Function call
    reverseusingfunction(arr2)
    # It will run till length of arr2 and print each item one by one
    print("By using reverse function: ")
    for i in range(len(arr2)):
        print(arr2[i] , end=  " ")
