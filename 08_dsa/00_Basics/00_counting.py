import math

N = 12345

# Brute force
def CountingNumber(n):
    count = 0 
    while n>0:
        count = count + 1 # Increse count by 1
        n = n // 10 # It will return integer value thats how it will remove last digit
    return count

# Optimal soulution
def CountingNumberWithLog(n):
    cnt = int(math.log10(n)+1)
    return cnt

print(f"\nBy Brute force solution")
print(f"The total degites in {N} is {CountingNumber(N)}.")
print(f"\nBy Optimal solution")
print(f"The total degites by using math.log10 on {N} is:{CountingNumberWithLog(N)}.")
