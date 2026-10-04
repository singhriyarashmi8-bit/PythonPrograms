def is_palindrome(n):
    if n < 0:
        return False
    original = str(n)
    return original == original[::-1]

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print(f"{num} is a Palindrome")
    else:
        print(f"{num} is not a Palindrome")