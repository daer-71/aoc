f = open("01/input01.txt", "r")
content = f.read()
lines = content.splitlines()
l1 = []
l2 = []
for l in lines:
    l1.append(l.split()[0])
    l2.append(l.split()[1])
#l1.sort()
#l2.sort()
lResult = 0
for l in l1:
    lResult += int(l) * l2.count(l)
print(lResult)
