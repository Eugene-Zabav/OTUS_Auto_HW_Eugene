import json
import csv


books_list = []
books_keys = ["Title", "Author", "Pages", "Genre"]

with open("books.csv", "r") as csv_file:
    for row in csv.DictReader(csv_file):
        data = {key: value for key, value in row.items() if key in books_keys}
        data = {key.lower(): data.pop(key) for key in books_keys}
        books_list.append(data)

with open("users.json", "r") as json_file:
    users_default = json.load(json_file)

users_list = []
users_keys = ["name", "gender", "address", "age"]

for i, user in enumerate(users_default):
    data = {key: value for key, value in users_default[i].items() if key in users_keys}
    data = {key: data.pop(key) for key in users_keys}
    users_list.append(data)

result_list = []
books_per_user = len(books_list) // len(users_default)
remaining_books = len(books_list) % len(users_default)

for i, user in enumerate(users_list):
    user_books = books_list[i * books_per_user : (i + 1) * books_per_user]
    if i < remaining_books:
        user_books.append(books_list[len(users_default) * books_per_user + i])
    user["books"] = user_books
    result_list.append(user)

with open("result.json", "w") as file:
    json.dump(result_list, file, indent=4)
    file.write("\n")
