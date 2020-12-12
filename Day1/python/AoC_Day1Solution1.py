
zahlen = []

with open("../Day1Input.txt") as f:
    for zeile in f:
        zahlen.append(int(zeile.strip()))
mysum = 0
for zahl in zahlen:
    res = zahl // 3 - 2
    mysum += res

print(mysum)
