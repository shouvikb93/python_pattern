n = int(input())      

for i in range(n):

    for j in range(2 * n - 1):
        if j == i or j == 2 * n - 2 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    for j in range(2 * n - 1):
        if i == 0 or i == n - 1 or j == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    for j in range(2 * n - 1):
        if i == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    for j in range(2 * n - 1):
        if i == 0 or i == n - 1 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()