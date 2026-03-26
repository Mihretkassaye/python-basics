print("=" * 50)
print("MY PYTHON LEARNING")
print("=" * 50)

print("\n--- PART 1: VARIABLES ---")

name = "Mihret"
age = 25
country = "Ethiopia"
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")

print("\n--- PART 2: LISTS ---")

fruits = ["apple", "banana", "orange"]
print(f"My fruits: {fruits}")
fruits.append("mango")
print(f"After adding mango: {fruits}")
print(f"First fruit: {fruits[0]}")

print("\n--- PART 3: DICTIONARIES ---")

person = {
    "name": "Mihret",
    "age": 25,
    "city": "Addis Ababa"
}
print(f"Person: {person}")
print(f"Name: {person['name']}")

print("\n--- PART 4: FUNCTIONS ---")

def greet(name):
    return f"Hello {name}!"

def add(a, b):
    return a + b

print(greet("Mihret"))
print(f"5 + 3 = {add(5, 3)}")

print("\n--- PART 5: LOOPS ---")

print("Numbers 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

print("\nMy fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

print("\n--- PART 6: CONDITIONALS ---")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score} -> Grade: {grade}")

print("\n--- PRACTICE 1: SIMPLE CALCULATOR ---")

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"

print(f"10 + 5 = {calculate(10, 5, '+')}")
print(f"10 - 5 = {calculate(10, 5, '-')}")
print(f"10 * 5 = {calculate(10, 5, '*')}")
print(f"10 / 5 = {calculate(10, 5, '/')}")

print("\n--- PRACTICE 2: STUDENT GRADES ---")

students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90
}

for student, score in students.items():
    if score >= 80:
        result = "Pass"
    else:
        result = "Need Improvement"
    print(f"{student}: {score} - {result}")

average = (85 + 72 + 90) / 3
print(f"Class average: {average:.1f}")

print("\n--- PRACTICE 3: SHOPPING LIST ---")

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"Added: {item}")

def show_list():
    print("My Shopping List:")
    for item in shopping_list:
        print(f"  - {item}")

add_item("milk")
add_item("bread")
add_item("eggs")
show_list()
print(f"Total items: {len(shopping_list)}")

print("\n--- PRACTICE 4: TEMPERATURE CONVERTER ---")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temps = [0, 20, 30, 100]
for c in temps:
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f}°F")

print("\n" + "=" * 50)
print("I'M READY FOR DATA SCIENCE BOOT CAMP")
print("=" * 50)
