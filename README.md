# Lambda Basics in Python

## What are Lambdas?

Lambdas are Python's implementation of anonymous functions.

## Basic Syntax

```Python
lambda arguments: expression
```

The literal "lambda" keyword begins a lambda function.

Arguments are comma-separated list of input parameters of the function.

Expression is a single expression whose result is implicitly returned.

## Examples

### Sorting a dictionary by key using a key function

```Python
def main():
    persons = create_list_of_persons()
    print_list(persons)

# sort by city key
def sort_by_city_key(person):
    return person["city"]

# print list sorted by city function to pass to sorted
def print_list(persons):
    for person in sorted(persons, key=sort_by_city_key):
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

# Output
# Susie is 59 years old and lives in Atlanta  
# Frank is 46 years old and lives in Chicago  
# George is 44 years old and lives in New York City    
```

### Sorting a dctionary by key using a lambda function

```Python
def main():
    persons = create_list_of_persons()
    print_list(persons)

# print list sorted by city using a lambda
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

# Output
# Susie is 59 years old and lives in Atlanta  
# Frank is 46 years old and lives in Chicago  
# George is 44 years old and lives in New York City    
```

## When to Use Lambdas?

Lambdas can be used when a small, one-time function is needed.  They are very useful where functions can be accepted as parameters to other functions.
