# Input from user
diamond_size = int(input("Enter diamond size (>=2): "))
rect_width = int(input("Enter rectangle width (odd number): "))
rect_height = int(input("Enter rectangle height (>=2): "))

# Ensure rectangle width is odd
if rect_width % 2 == 0:
    rect_width += 1
    print(f"Width changed to {rect_width} so that it has an exact center.")

center = rect_width // 2

# -------------------
# Upper half diamond
# -------------------
for i in range(diamond_size):

    # Leading spaces to align with rectangle center
    print(" " * (center - i), end="")

    print("*", end="")

    if i > 0:
        print(" " * (2 * i - 1), end="")
        print("*", end="")

    print()

# -------------------
# Lower half diamond
# -------------------
for i in range(diamond_size - 2, -1, -1):

    print(" " * (center - i), end="")

    print("*", end="")

    if i > 0:
        print(" " * (2 * i - 1), end="")
        print("*", end="")

    print()

# -------------------
# Rectangle
# -------------------
for i in range(rect_height):

    for j in range(rect_width):

        if i == 0 or i == rect_height - 1 or j == 0 or j == rect_width - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()