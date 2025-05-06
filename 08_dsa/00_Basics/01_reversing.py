def ReversedNumber(n):
    rev = 0
    while n>0:
        rem = n % 10 # it will store the last digit
        rev = rev * 10 + rem # here it will multiply rev with 10 and add the reminder means 0 * 10 + 5 which will return 5 
        n = n//10 # it will remove the last digit of n
        
    return rev


N = 12345
print(f"The reversed of number {N} is:", ReversedNumber(N))