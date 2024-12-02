f = open("01/input01.txt", "r")
content = f.read()
lines = content.splitlines()
l1 = []
l2 = []
for l in lines:
    l1.append(l.split()[0])
    l2.append(l.split()[1])
l1.sort()
l2.sort()
lResult = 0
for i in range(len(l1)):
    lResult += abs(int(l1[i]) - int(l2[i]))
print(lResult)
