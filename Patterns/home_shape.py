n = int(input())

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()

height = int(input())
width = 2 * n - 1

for i in range(1, height):

    for j in range(width):

        if i == height - 1 or j == 0 or j == width - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()