# # print binary , octal, hexadec of a binary number in a table format (like the books in B ghosh)

# def print_formatted(number):
#     # your code goes here
    

#     width = len(bin(number)[2:])

#     for i in range(1, number + 1):

#         decimal = str(i)
#         octal = oct(i)[2:]
#         hexadecimal = hex(i)[2:].upper()
#         binary = bin(i)[2:]

#         print(
#             decimal.rjust(width),
#             octal.rjust(width),
#             hexadecimal.rjust(width),
#             binary.rjust(width)
#         )
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


#without using the inbuilt bin(), oct(), hex() functions


def decimal_to_binary(num):

    if num == 0:
        return "0"

    binary = ""

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    return binary


def decimal_to_octal(num):

    if num == 0:
        return "0"

    octal = ""

    while num > 0:
        octal = str(num % 8) + octal
        num //= 8

    return octal


def decimal_to_hexadecimal(num):

    if num == 0:
        return "0"

    digits = "0123456789ABCDEF"

    hexadecimal = ""

    while num > 0:
        remainder = num % 16
        hexadecimal = digits[remainder] + hexadecimal
        num //= 16

    return hexadecimal


def print_formatted(number):

    width = len(decimal_to_binary(number))

    for i in range(1, number + 1):

        decimal = str(i)
        octal = decimal_to_octal(i)
        hexadecimal = decimal_to_hexadecimal(i)
        binary = decimal_to_binary(i)

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexadecimal.rjust(width),
            binary.rjust(width)
        )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)