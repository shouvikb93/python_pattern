#count the number of each vowel in a given string from user

text = input("Enter a string: ")
text = text.lower()

visited = ""

for i in range(len(text)):

    if text[i] in "aeiou":

        if text[i] not in visited:

            count = 0

            for j in range(len(text)):

                if text[i] == text[j]:
                    count += 1

            print(text[i], ":", count)

            visited += text[i]