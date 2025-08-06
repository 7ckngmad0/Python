# ============================================
# PYTHON TUTORIAL FOR BEGINNERS
# ============================================
# This tutorial covers essential Python concepts
# for beginners with examples and explanations
# PARANG CHEAT SHEET LANG TO GUYSSSS, ASK NALANG KAYO SAKIN PAG MAY DI KAYO MA-GETS THANKYOOOOOUUUUUUUUUUUUUUU

print("Welcome to Python Tutorial for Beginners!")
print("=" * 50)

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

print("\n1. VARIABLES AND DATA TYPES")
print("-" * 30)

# Integer - whole numbers
age = 25
print(f"Age: {age} (type: {type(age)})")

# Float - decimal numbers
height = 5.8
print(f"Height: {height} (type: {type(height)})")

# String - text (use quotes)
name = "Alice"
print(f"Name: {name} (type: {type(name)})")

# Boolean - True or False
is_student = True
print(f"Is student: {is_student} (type: {type(is_student)})")

# List - ordered collection (mutable)
fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits} (type: {type(fruits)})")

# Tuple - ordered collection (immutable)
coordinates = (10, 20)
print(f"Coordinates: {coordinates} (type: {type(coordinates)})")

# Dictionary - key-value pairs
person = {"name": "Bob", "age": 30, "city": "New York"}
print(f"Person: {person} (type: {type(person)})")

# ============================================
# 2. F-STRINGS (FORMATTED STRINGS)
# ============================================

print("\n2. F-STRINGS (FORMATTED STRINGS)")
print("-" * 30)

# F-strings are a modern way to format strings in Python
# Use 'f' before the string and {} to insert variables

first_name = "John"
last_name = "Doe"
age = 30

# Basic f-string
print(f"My name is {first_name} {last_name}")

# F-string with expressions
print(f"I am {age} years old")

# F-string with calculations
birth_year = 1994
current_year = 2024
print(f"I was born in {birth_year} and I am {current_year - birth_year} years old")

# F-string with formatting
price = 19.99
print(f"The price is ${price:.2f}")  # .2f means 2 decimal places

# F-string with multiple variables
city = "Boston"
country = "USA"
print(f"I live in {city}, {country}")

# ============================================
# 3. IF-ELSE STATEMENTS
# ============================================

print("\n3. IF-ELSE STATEMENTS")
print("-" * 30)

# Basic if statement
temperature = 75

if temperature > 80:
    print("It's hot outside!")
elif temperature > 60:
    print("It's nice weather!")
else:
    print("It's cold outside!")

# If-else with multiple conditions
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Nested if statements
age = 18
has_license = True

if age >= 16:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license to drive.")
else:
    print("You're too young to drive.")

# ============================================
# 4. WHILE LOOPS
# ============================================

print("\n4. WHILE LOOPS")
print("-" * 30)

# Basic while loop
print("Counting from 1 to 5:")
counter = 1
while counter <= 5:
    print(f"Count: {counter}")
    counter += 1  # Same as counter = counter + 1

# While loop with break
print("\nGuessing game (1-10):")
import random
secret_number = random.randint(1, 10)
attempts = 0

while True:
    attempts += 1
    guess = random.randint(1, 10)  # Simulating user input
    
    if guess == secret_number:
        print(f"Correct! Found in {attempts} attempts")
        break
    elif guess < secret_number:
        print(f"Too low! ({attempts} attempts)")
    else:
        print(f"Too high! ({attempts} attempts)")

# While loop with continue
print("\nPrinting even numbers from 1 to 10:")
number = 1
while number <= 10:
    if number % 2 != 0:  # If number is odd
        number += 1
        continue  # Skip to next iteration
    print(f"Even number: {number}")
    number += 1

# ============================================
# 5. FOR LOOPS
# ============================================

print("\n5. FOR LOOPS")
print("-" * 30)

# For loop with range()
print("Counting with range:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Number: {i}")

print("\nCounting with range(start, stop):")
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(f"Number: {i}")

# For loop with list
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# For loop with enumerate (get index and value)
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# For loop with dictionary
person = {"name": "Alice", "age": 25, "city": "Boston"}
print("\nPerson details:")
for key, value in person.items():
    print(f"{key}: {value}")

# ============================================
# 6. FUNCTIONS
# ============================================

print("\n6. FUNCTIONS")
print("-" * 30)

# Basic function
def greet(name):
    """This function greets the person passed in as a parameter"""
    return f"Hello, {name}!"

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

# Function with multiple return values
def get_name_and_age():
    return "John", 30

# Testing functions
print(greet("Alice"))
print(f"5 + 3 = {add_numbers(5, 3)}")
print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# ============================================
# 7. LISTS AND LIST METHODS
# ============================================

print("\n7. LISTS AND LIST METHODS")
print("-" * 30)

# Creating lists
numbers = [1, 2, 3, 4, 5]
colors = ["red", "green", "blue"]

# Adding elements
numbers.append(6)  # Add to end
print(f"After append: {numbers}")

numbers.insert(0, 0)  # Insert at specific position
print(f"After insert: {numbers}")

# Removing elements
numbers.remove(3)  # Remove specific value
print(f"After remove: {numbers}")

popped = numbers.pop()  # Remove and return last element
print(f"Popped: {popped}, List: {numbers}")

# List operations
print(f"Length: {len(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")

# List comprehension (advanced but useful)
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# ============================================
# 8. NUMPY BASICS
# ============================================

print("\n8. NUMPY BASICS")
print("-" * 30)

# First, we need to import numpy
try:
    import numpy as np
    print("NumPy imported successfully!")
    
    # Creating arrays
    print("\nCreating NumPy arrays:")
    
    # 1D array
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f"1D array: {arr1d}")
    print(f"Shape: {arr1d.shape}")
    print(f"Data type: {arr1d.dtype}")
    
    # 2D array (matrix)
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n2D array:\n{arr2d}")
    print(f"Shape: {arr2d.shape}")
    
    # Creating arrays with specific values
    zeros = np.zeros(5)  # Array of zeros
    print(f"\nZeros: {zeros}")
    
    ones = np.ones((3, 3))  # 3x3 matrix of ones
    print(f"Ones:\n{ones}")
    
    # Range array
    range_arr = np.arange(0, 10, 2)  # Start, stop, step
    print(f"Range: {range_arr}")
    
    # Linspace (evenly spaced numbers)
    linspace_arr = np.linspace(0, 1, 5)  # Start, stop, number of points
    print(f"Linspace: {linspace_arr}")
    
    # Array operations
    print("\nArray operations:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a + b: {a + b}")
    print(f"a * b: {a * b}")  # Element-wise multiplication
    print(f"a ** 2: {a ** 2}")  # Element-wise power
    
    # Statistical operations
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"\nData: {data}")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard deviation: {np.std(data)}")
    print(f"Min: {np.min(data)}")
    print(f"Max: {np.max(data)}")
    
    # Reshaping arrays
    arr = np.arange(12)
    print(f"\nOriginal array: {arr}")
    
    reshaped = arr.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped}")
    
    # Indexing and slicing
    print(f"\nFirst element: {arr[0]}")
    print(f"Last element: {arr[-1]}")
    print(f"First 5 elements: {arr[:5]}")
    print(f"Elements 2 to 7: {arr[2:8]}")
    
    # 2D array indexing
    print(f"\n2D array:\n{reshaped}")
    print(f"Element at row 1, column 2: {reshaped[1, 2]}")
    print(f"First row: {reshaped[0, :]}")
    print(f"Second column: {reshaped[:, 1]}")
    
except ImportError:
    print("NumPy is not installed. Install it with: pip install numpy")

# ============================================
# 9. PRACTICAL EXAMPLES
# ============================================

print("\n9. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Grade calculator
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [85, 92, 78, 96, 88]
print("Grade calculator:")
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score} -> Grade: {grade}")

# Example 2: Simple calculator
def calculator():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = 2  # Simulating user input
    num1, num2 = 10, 5
    
    if choice == 1:
        result = num1 + num2
        operation = "+"
    elif choice == 2:
        result = num1 - num2
        operation = "-"
    elif choice == 3:
        result = num1 * num2
        operation = "*"
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            operation = "/"
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid choice!"
    
    return f"{num1} {operation} {num2} = {result}"

print(calculator())

# Example 3: Number guessing game
def number_guessing_game():
    import random
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"\nNumber Guessing Game (1-100)")
    print(f"You have {max_attempts} attempts")
    
    while attempts < max_attempts:
        attempts += 1
        guess = random.randint(1, 100)  # Simulating user input
        
        if guess == secret:
            return f"Congratulations! You found it in {attempts} attempts!"
        elif guess < secret:
            print(f"Too low! ({max_attempts - attempts} attempts left)")
        else:
            print(f"Too high! ({max_attempts - attempts} attempts left)")
    
    return f"Game over! The number was {secret}"

print(number_guessing_game())

# ============================================
# 10. BEST PRACTICES AND TIPS
# ============================================

print("\n10. BEST PRACTICES AND TIPS")
print("-" * 30)

print("""
1. Use meaningful variable names
   - Good: user_age, total_score
   - Bad: a, x, temp

2. Write comments to explain your code
   - Use # for single line comments
   - Use ''' or \"\"\" for multi-line comments

3. Use proper indentation (4 spaces)
   - Python is sensitive to indentation
   - Use consistent spacing

4. Handle errors with try-except
   - Always validate user input
   - Handle potential errors gracefully

5. Use functions to organize code
   - Break complex tasks into smaller functions
   - Make code reusable

6. Use f-strings for string formatting
   - More readable than .format() or %
   - Available in Python 3.6+

7. Use list comprehensions when appropriate
   - More concise than for loops
   - Good for simple transformations

8. Import libraries at the top of your file
   - Keep imports organized
   - Use specific imports when possible
""")

print("\n" + "=" * 50)
print("Congratulations! You've completed the Python tutorial!")
print("Keep practicing and building projects to improve your skills.")
print("=" * 50)
