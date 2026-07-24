tree_height = int(input("Enter tree height: "))
trunk_height = int(input("Enter trunk height: "))
trunk_width = int(input("Enter trunk width (odd): "))

if trunk_width % 2 == 0:
    trunk_width += 1

# Leaves
for i in range(1, tree_height + 1):

    for j in range(tree_height - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Trunk
spaces = tree_height - (trunk_width // 2) - 1

for i in range(trunk_height):

    for j in range(spaces):
        print(" ", end="")

    for j in range(trunk_width):
        print("*", end="")

    print()