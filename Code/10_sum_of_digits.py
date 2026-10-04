def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(num))