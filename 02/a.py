f = open("02/input02.txt", "r")
content = f.read()
reports = content.splitlines()

for reportLine in reports:
    report = reportLine.split()
    print(report)
    diffs = [int(report[i+1]) - int(report[i]) for i in range(len(report) - 1)]
    print(diffs)
    diff = [int(diffs[i+1]) - int(diffs[i]) for i in range(len(diffs) - 1)]
