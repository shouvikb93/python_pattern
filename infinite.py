# i=5
# while i<6:
# 	print(i)
# 	i=i-1
# print("loop ended")


limit = int(input("Enter stopping count: "))

count = 0

while True:
    print("Loop Count =", count)

    if count == limit:
        break

    count += 1

print("Loop stopped.")