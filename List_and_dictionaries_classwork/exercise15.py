student = {
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"
}

key = input("Enter a Key:")

for key in student:
    print(key, "exists in the dictionary")
else:
    print(key, "does not exists in the dictionary")
    