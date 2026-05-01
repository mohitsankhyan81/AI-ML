import json

name = input("Enter your name: ")
age = int(input("Enter your age: "))

def data(name, age):
    data1 = {
        "name": name,
        "age": age
    }

    with open("data.json", "a") as f:
        json.dump(data1, f, indent=4)
        f.write("\n")

    print("Saved:", data1)

data(name, age)