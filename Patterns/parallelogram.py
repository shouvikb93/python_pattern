rows = 5
cols = 8

for i in range(rows):

    for j in range(rows-i):
        print(" ", end="")

    for j in range(cols):
        print("*", end="")

    print()