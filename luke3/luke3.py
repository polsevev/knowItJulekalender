f = open("wordlist.txt", "r")
g = open("matrix.txt", "r")

listOfDiagonals = []
diagonals2 = []
matrix = []
words = []
wordsToRemove = []
matrixMoved = []

for i in range(0, 1000):
    matrix.append(g.readline().strip())

for i in range(25):
    words.append(f.readline().strip())

for i in range(len(matrix)):
    for b in words:
        if b in matrix[i]:
            wordsToRemove.append(b)
        if b in matrix[i][::-1]:
            wordsToRemove.append(b)


for i in range(len(matrix)):
    curString = ""
    for b in range(len(matrix[i])):
        if 0 <= b < len(matrix) and 0 <= i < len(matrix):
            curString += matrix[b][i]
    for c in words:
        if c in curString:
           if c not in wordsToRemove:
               wordsToRemove.append(c)
        if c in curString[::-1]:
            if c not in wordsToRemove:
                wordsToRemove.append(c)

for x in range(len(matrix)):
    curString = ""
    counter = 0
    for y in range(len(matrix)-x-1, -1, -1):
        curString += matrix[y][counter]
        counter+=1
    listOfDiagonals.append(curString)
    counter = 0
    curString = ""
    for y in range(len(matrix)+x, 0, -1):
        if 0 <= y < len(matrix) and counter < len(matrix):
            curString += matrix[y][counter]
        counter += 1
    listOfDiagonals.append(curString)




for y in range(len(matrix)):
    curString = ""
    counter = 0
    for x in range(len(matrix)-y-1, len(matrix)):
        if x < len(matrix) and x >= 0:
            curString += matrix[counter][x]
        counter += 1
    listOfDiagonals.append(curString)
    counter = 0
    curString = ""
    for x in range(-y, len(matrix)):
        if 0 <= x < len(matrix) and counter < len(matrix):
            curString += matrix[counter][x]
        counter += 1
    listOfDiagonals.append(curString)

for x in listOfDiagonals:
    for c in words:      
        if c in x:
            if c not in wordsToRemove:
                wordsToRemove.append(c)
        if c in x[::-1]:
            if c not in wordsToRemove:
                wordsToRemove.append(c)


for i in wordsToRemove:
    if i not in words:
        continue
    words.remove(i)
print(",".join(words))
print(wordsToRemove)
