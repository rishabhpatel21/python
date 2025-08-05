def check_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage:
s = "A man, a plan, a canal: Panama"
print(check_palindrome(s))  # Output: True

