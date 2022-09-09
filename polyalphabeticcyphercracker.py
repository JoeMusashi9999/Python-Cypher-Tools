#arrays to use
shiftsequence = []
output = []

#user prompt
print("type in cypher")
x = input()
print("type in cypher word")
y = input()
shiftsequencething = y
#we split the strings into arrays
letters = x.split(" ")


#put the shift in an array
for item in shiftsequencething:
    shiftsequence.append(ord(item)%32)


for item in letters:
    #debug -remove after
    print(item)
    i = 0
    if i % 6 == 0:
        string = ord(letters[i]) - ord('a') + int(shiftsequence[0])
        #output.append(string.ascii_letters[index % len(string.ascii_letters)])
    if i % 6 == 1:
        string = ord(letters[i]) - ord('a') + int(shiftsequence[1])
        #output.append(string.ascii_letters[index % len(string.ascii_letters)])
    if i % 6 == 2:
        string = ord(letters[i]) - ord('a') + int(shiftsequence[2])
        #output.append(string.ascii_letters[index % len(string.ascii_letters)])
    if i % 6 == 3:
        string = ord(letters[i]) - ord('a') + int(shiftsequence[3])
        #output.append(string.ascii_letters[index % len(string.ascii_letters)])
    if i % 6 == 4:
        string = ord(letters[i]) - ord('a') + int(shiftsequence[4])
        #output.append(string.ascii_letters[index % len(string.ascii_letters)])
    if i % 6 == 5:
        string = ord(letters[i]) - ord('a') + int(shiftsequence[5])
        #output.append(string.ascii_letters[index % len(string.ascii_letters)])
    if i % 6 == 6:
        string = ord(letters[i]) - ord('a') + int(shiftsequence[6])
        #output.append(string.ascii_letters[index % len(string.ascii_letters)])

#debug
print(letters)
print(shiftsequence)
print(len(letters))
