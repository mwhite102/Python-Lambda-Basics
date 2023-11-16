def main():
    persons = create_list_of_persons()
    print_list(persons)

# print list sorted by city
def print_list(persons):
    for person in sorted(persons, key=lambda person: person["city"]):
        print(f"{person['name']} is {person['age']} years old and lives in {person['city']}  ")

# get mock data
def create_list_of_persons():
    list = []
    list.append({"name": "George", "age": 44, "city" : "New York City"})
    list.append({"name": "Frank", "age": 46, "city" : "Chicago"})
    list.append({"name": "Susie", "age": 59, "city" : "Atlanta"})
    return list

if __name__ == "__main__":
    main();