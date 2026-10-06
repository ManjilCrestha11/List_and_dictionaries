marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}

for name, mark in marks.items():
    print(name, "-", mark)

total = sum(marks.values())
average = total / len(marks)
highest = max(marks.values())
lowest = min(marks.values())

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

for name, mark in marks.items():
    if mark == highest:
        print("Highest student:", name)