import json

category = ["Food", "Salary", "Gift", "Miscellaneous", "Transport", "Delivery", "Travel", "Cafe"]


def load():
    all_data = []
    try:
        with open("data.json", "r", encoding="utf-8") as file1:
            all_data = json.load(file1)
    except FileNotFoundError:
        print("Create new file!")
    return all_data

def save(all_data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(all_data, file, ensure_ascii=False, indent=2)
    print("Operation saved successfully!")
    print(all_data)