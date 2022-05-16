conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def decimal_to_hexadecimal(decimal):
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        print("remainder", remainder)
        print("conversion",conversion_table[remainder])
        print("hexadecimal",hexadecimal)
        hexadecimal = conversion_table[remainder] + hexadecimal

        decimal = decimal // 16
    return hexadecimal


if __name__ == "__main__":
    decimal = 1087
    print(decimal_to_hexadecimal(decimal))
