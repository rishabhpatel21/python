def check_palindrome(arr):
    # using two pointers to check if the array is a palindrome
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage:
arr = [1, 2, 3, 2, 1]
print(check_palindrome(arr))  # Output: True

