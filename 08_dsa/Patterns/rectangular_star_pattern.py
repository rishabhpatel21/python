def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("")
    pass

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    pattern1(num)