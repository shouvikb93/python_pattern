n = 5

for i in range(n):

    for j in range(n - i):
        print(" ", end="")

    value = 1

    for j in range(i + 1):

        print(value, end=" ")

        value = value * (i - j) // (j + 1)

    print()