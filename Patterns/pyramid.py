n=5

for i in range(1, n+1):

    for j in range(1, i + 1):

        print(i, end=" ")

    print()

for i in range(n,-1,-1):

    for j in range(1, i):

        print(i, end=" ")

    print()
 