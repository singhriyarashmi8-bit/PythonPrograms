def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Reversed Number:", reverse_number(num))