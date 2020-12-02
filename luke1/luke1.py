f = open("numbers.txt", "r")

liste = []
for i in range(1, 100001):
    liste.append(i)

liste2 = f.read().split(",")

for x in liste2:
    liste.remove(int(x))

print(liste)