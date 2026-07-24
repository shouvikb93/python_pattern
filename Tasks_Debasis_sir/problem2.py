#count occurances of character in a string

string = input("Enter a string: ")

visited = ""

for i in range(len(string)):

    if string[i] not in visited:

        count = 0

        for j in range(len(string)):

            if string[i] == string[j]:
                count += 1

        print(string[i], ":", count)

        visited += string[i]