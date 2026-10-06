marks =[75, 82, 68, 90, 55, 88, 72, 95]

print("Marks:", marks)
print("Total Marks:", sum(marks))
print("Average:", sum(marks)/len(marks))
print("Highest:", max(marks))
print("Smallest:", min(marks))

count = 0

for mark in marks:
    if mark <=75:
        count +=1
    print("Marks above 75", count);

marks.sort(reverse=True)
print("highest to lowest:", marks)
