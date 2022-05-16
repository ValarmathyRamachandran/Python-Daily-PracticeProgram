def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        return "The entered number is a perfect number"
    else:
        return "The entered number is not a perfect number"


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    print(perfect_number(num))
