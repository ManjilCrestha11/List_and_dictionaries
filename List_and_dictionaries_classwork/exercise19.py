students = {
    101: {
        "name": "Ram",
        "age": 20,
        "course": "Python"
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "Java"
    },
    103: {
        "name": "Hari",
        "age": 19,
        "course": "Python"
    }
}

print("All students:")
print(students)

print("Student 102:")
print(students[102])

students[103]["course"] = "Data Science"

students[104] = {
    "name": "Gita",
    "age": 20,
    "course": "Python"
}

del students[101]

print("Final dictionary:")
print(students)