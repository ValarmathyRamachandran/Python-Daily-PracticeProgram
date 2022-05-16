def binaryToDecimal(binary):
    binary1 = int(binary)
    decimal, i, n = 0, 0, 0

    while binary1 != 0:
        dec = binary1 % 10
        decimal = decimal + dec * pow(2, i)
        binary1 = binary1 // 10
        i += 1
    return decimal


def decToHexa(n):
    # char array to store
    # hexadecimal number
    hexaDeciNum = ['0'] * 100

    # counter for hexadecimal
    # number array
    i = 0
    while n != 0:

        # temporary variable
        # to store remainder
        temp = 0

        # storing remainder
        # in temp variable.
        temp = n % 16

        # check if temp < 10
        if temp < 10:
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)

    # printing hexadecimal number
    # array in reverse order
    j = i - 1
    while j >= 0:
        print((hexaDeciNum[j]), end="")
        j = j - 1
    print()


# function to convert binary to
# hexadecimal
def binToHexa(n):
    decimal = binaryToDecimal(n)
    print("Hexadecimal equivalent of {}: ".format(n))
    decToHexa(decimal)


if __name__ == '__main__':
    binToHexa('1111')
    binToHexa('110101')
    binToHexa('100001111')
    binToHexa('111101111011')
