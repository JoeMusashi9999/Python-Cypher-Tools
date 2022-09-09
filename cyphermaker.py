import string
output = []
text = input("type something> ")
shift = int(input("enter number of shifts> "))
for letter in text:
    index = ord(letter) - ord('a') + shift
    output.append(string.ascii_letters[index % len(string.ascii_letters)])
print(output)
