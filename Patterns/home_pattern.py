roof_height = int(input("Enter roof height: "))
house_width = int(input("Enter house width (odd): "))
house_height = int(input("Enter house height: "))


if house_width % 2 == 0:
    house_width += 1
    print("Width changed to", house_width)

center = house_width // 2


for i in range(roof_height):

    for j in range(center - i):
        print(" ", end="")

    for j in range(2 * i + 1):

        if j == 0 or j == 2 * i or i == roof_height - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()


for i in range(house_height):

    for j in range(house_width):

        if i == 0 or i == house_height - 1 or j == 0 or j == house_width - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()