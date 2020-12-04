f = open("leveringsliste.txt", "r")

fil = f.readlines()

dic = {
    "sukker" : 0,
    "mel": 0,
    "melk":0,
    "egg":0
}

for i in range(len(fil)):
    fil[i] = fil[i].strip().split(" ")

for i in range(len(fil)):
    for b in range(len(fil[i])):
        fil[i][b] = fil[i][b].replace(":", "")
        fil[i][b] = fil[i][b].replace(",", "")

for i in fil:
    for b in range(0, len(i), 2):
        dic[i[b]] += int(i[b+1])

counter = 0
while True:
    if dic["sukker"] < 2 or dic["mel"] < 3 or dic["melk"] < 3 or dic["egg"] < 1:
        break
    counter += 1
    dic["sukker"] -= 2
    dic["mel"] -= 3
    dic["melk"] -= 3
    dic["egg"] -= 1

print(counter)