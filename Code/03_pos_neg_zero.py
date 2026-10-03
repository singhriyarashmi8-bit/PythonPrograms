def check_pos_neg_zero(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    print(check_pos_neg_zero(num))