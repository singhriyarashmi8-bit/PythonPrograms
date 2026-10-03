def find_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial is:", find_factorial(num))