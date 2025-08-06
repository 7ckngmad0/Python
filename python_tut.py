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

# Unlike C, Python is dynamically typed - no need to declare types
# Variables are created when you assign values
# Hindi mo na kailangan mag int x = 5; or float y = 2.5; diretso assign lang dito, bes!

# Integer
age = 25  # parang int sa C, pero walang limit, kahit gaano kalaki
print(f"Age: {age} (type: {type(age)})")

# Float (para na rin siyang double sa C)
height = 5.8  # decimal, walang float x = 5.8; dito, diretso na
print(f"Height: {height} (type: {type(height)})")

# String (like char* in C, pero mas madali gamitin dito)
name = "Alice"  # string, kahit anong text, basta naka-quotes
print(f"Name: {name} (type: {type(name)})")

# Boolean
is_student = True # naka capitalized talaga dapat yang T, wag mo kalimutan!
print(f"Is student: {is_student} (type: {type(is_student)})")

# List - dynamic array
fruits = ["apple", "banana", "orange"]  # parang array, pero pwede dagdag/bawas kahit kailan
print(f"Fruits: {fruits} (type: {type(fruits)})")

# Tuple - immutable list (like const array in C)
coordinates = (10, 20)  # parang array na di mo na pwede baguhin
print(f"Coordinates: {coordinates} (type: {type(coordinates)})")

# Dictionary - hash table (like struct with key-value pairs)
person = {"name": "Bob", "age": 30, "city": "New York"}  # parang struct, pero key-value style
print(f"Person: {person} (type: {type(person)})")

# ============================================
# 2. F-STRINGS (FORMATTED STRINGS)
# ============================================

print("\n2. F-STRINGS (FORMATTED STRINGS)")
print("-" * 30)

# Much cleaner than printf() or sprintf() in C
# Use 'f' before the string and {} to insert variables
# Sobrang dali maglagay ng variable sa string, hindi na kailangan ng %d, %s, etc. Galing diba?

first_name = "John"
last_name = "Doe"
age = 30

# Basic f-string (like printf na may scanf, but simpler)
print(f"My name is {first_name} {last_name}")  # O diba, walang kahirap-hirap!

# F-string with expressions (pwede ka mag-math sa loob ng {})
print(f"I am {age} years old")

# F-string with calculations (no need for temporary variables)
birth_year = 1994
current_year = 2024
print(f"I was born in {birth_year} and I am {current_year - birth_year} years old")  # Automatic na yan!

# F-string with formatting (like %.2f sa C, yung : ang nag i-indicate ng formatting)
price = 19.99
print(f"The price is ${price:.2f}")  # .2f means 2 decimal places, pang money format

# F-string with multiple variables
city = "Boston"
country = "USA"
print(f"I live in {city}, {country}")

# ============================================
# 3. IF-ELSE STATEMENTS
# ============================================

print("\n3. IF-ELSE STATEMENTS")
print("-" * 30)

# Python if-else syntax is similar to C, pero elif ginagamit not else if
# No parentheses needed around conditions (pero ok lang din naman)
# Indentation lang, walang braces! Wag kalimutan mag-indent, bes!

# Basic if statement (like C but no braces, use INDENTATION)
temperature = 75

if temperature > 80:
    print("It's hot outside!")
elif temperature > 60:
    print("It's nice weather!")
else:
    print("It's cold outside!")

# If-else with multiple conditions (parang switch-case sa C, pero mas madali basahin)
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

# Nested if statements (same as C, pero may INDENTATION)
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

# Python while loops are very similar to C while loops
# Main difference: no braces, use INDENTATION
# Basta mag-indent ka lang, ok na!

# Basic while loop (like C while loop)
print("Counting from 1 to 5:")
counter = 1
while counter <= 5:
    print(f"Count: {counter}")
    counter += 1  # Same as counter++ or yung increment na tinatawag sa C

# While loop with break (same as C break)
print("\nGuessing game (1-10):")
import random
secret_number = random.randint(1, 10)
attempts = 0

while True:  # while(1) in C (1 yung true sa mga programming language)
    attempts += 1
    guess = random.randint(1, 10)  # Simulating user input
    
    if guess == secret_number:
        print(f"Correct! Found in {attempts} attempts")
        break 
    elif guess < secret_number:
        print(f"Too low! ({attempts} attempts)")
    else:
        print(f"Too high! ({attempts} attempts)")

# While loop with continue (same as C continue)
print("\nPrinting even numbers from 1 to 10:")
number = 1
while number <= 10:
    if number % 2 != 0:  # If number is odd
        number += 1
        continue  # skip na agad sa next loop
    print(f"Even number: {number}")
    number += 1

# ============================================
# 5. FOR LOOPS
# ============================================

print("\n5. FOR LOOPS")
print("-" * 30)

# Python for loops are more flexible than C for loops
# They iterate over sequences (lists, strings, etc.)

# For loop with range() (like C for loop with counter)
print("Counting with range:")
for i in range(5):  # 0, 1, 2, 3, 4 (like for(int i=0; i<5; i++) in C)
    print(f"Number: {i}")

print("\nCounting with range(start, stop):")
for i in range(1, 6):  # 1, 2, 3, 4, 5 (like for(int i=1; i<6; i++) in C)
    print(f"Number: {i}")

# For loop with list (like foreach in other languages)
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in the basket:")
for fruit in fruits:  # Iterates through each element
    print(f"- {fruit}")

# For loop with enumerate (get index and value - like C with counter)
print("\nFruits with index:")
for index, fruit in enumerate(fruits):  # enumerate() gives (index, value) pairs
    print(f"{index + 1}. {fruit}")  # May index na agad, hindi mo na kailangan mag-manual count

# For loop with dictionary (iterate through key-value pairs)
person = {"name": "Alice", "age": 25, "city": "Boston"}
print("\nPerson details:")
for key, value in person.items():  # .items() gives (key, value) pairs
    print(f"{key}: {value}")  # Parang struct, pero mas madali gamitin

# ============================================
# 6. FUNCTIONS
# ============================================

print("\n6. FUNCTIONS")
print("-" * 30)

# Python functions are similar to C functions but more flexible
# No need to declare return types or parameter types
# def lang, tapos pangalan ng function, tapos parameters. Walang int, void, char, etc.

# Basic function (like C function but no return type declaration)
def greet(name):
    """This function greets the person passed in as a parameter"""
    return f"Hello, {name}!"

# Function with multiple parameters (like C function parameters)
def add_numbers(a, b):
    return a + b

# Function with default parameters (no equivalent in C)
def greet_with_title(name, title="Mr."):  # Default value for title, parang optional parameter
    return f"Hello, {title} {name}!"

# Function with multiple return values (use tuples - no equivalent in C)
def get_name_and_age():
    return "John", 30  # Returns a tuple (name, age), parang sabay na return

# Testing functions
print(greet("Alice"))
print(f"5 + 3 = {add_numbers(5, 3)}")
print(greet_with_title("Smith"))  # Uses default title
print(greet_with_title("Johnson", "Dr."))  # Overrides default
name, age = get_name_and_age()  # Unpacking the returned tuple, parang auto assign
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

numbers.insert(0, 0)  # Insert at specific position, parang insert sa simula
print(f"After insert: {numbers}")

# Removing elements
numbers.remove(3)  # Remove specific value, hanapin niya tapos tanggalin
print(f"After remove: {numbers}")

popped = numbers.pop()  # Remove and return last element
print(f"Popped: {popped}, List: {numbers}")

# List operations
print(f"Length: {len(numbers)}")  # Gusto mo malaman ilang laman? len() lang!
print(f"Max: {max(numbers)}")     # Pinakamalaki
print(f"Min: {min(numbers)}")     # Pinakamaliit
print(f"Sum: {sum(numbers)}")     # Total ng lahat

# List comprehension (advanced but useful)
squares = [x**2 for x in range(5)]  # Gawa agad ng list ng squares, parang loop na one-liner
print(f"Squares: {squares}")

# ============================================
# 8. NUMPY BASICS
# ============================================

print("\n8. NUMPY BASICS")
print("-" * 30)

# NumPy is Python's numerical computing library
# Provides efficient array operations (like MATLAB or R)
# Much faster than Python lists for numerical operations

# First, we need to import numpy
try:
    import numpy as np
    print("NumPy imported successfully!")
    
    # Creating arrays
    print("\nCreating NumPy arrays:")
    
    # 1D array (like C array but with more features)
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f"1D array: {arr1d}")
    print(f"Shape: {arr1d.shape}")  # Array dimensions
    print(f"Data type: {arr1d.dtype}")  # Data type (like C types)
    
    # 2D array (matrix - like 2D array in C)
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n2D array:\n{arr2d}")
    print(f"Shape: {arr2d.shape}")
    
    # Creating arrays with specific values (no C equivalent)
    zeros = np.zeros(5)  # Array of zeros [0, 0, 0, 0, 0], parang memset sa C pero mas madali
    print(f"\nZeros: {zeros}")
    
    ones = np.ones((3, 3))  # 3x3 matrix of ones, parang puro 1 na matrix
    print(f"Ones:\n{ones}")
    
    # Range array (like for loop range)
    range_arr = np.arange(0, 10, 2)  # Start, stop, step
    print(f"Range: {range_arr}")
    
    # Linspace (evenly spaced numbers - no C equivalent)
    linspace_arr = np.linspace(0, 1, 5)  # Start, stop, number of points
    print(f"Linspace: {linspace_arr}")
    
    # Array operations (vectorized operations - much faster than C loops)
    print("\nArray operations:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a + b: {a + b}")  # Element-wise addition, parang sabay sabay na add
    print(f"a * b: {a * b}")  # Element-wise multiplication, hindi matrix multip to ah
    print(f"a ** 2: {a ** 2}")  # Element-wise power, parang lahat naka-square
    
    # Statistical operations (built-in functions)
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"\nData: {data}")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard deviation: {np.std(data)}")
    print(f"Min: {np.min(data)}")
    print(f"Max: {np.max(data)}")
    
    # Reshaping arrays (change dimensions)
    arr = np.arange(12)
    print(f"\nOriginal array: {arr}")
    
    reshaped = arr.reshape(3, 4)  # Reshape to 3x4 matrix, parang 2D array
    print(f"Reshaped to 3x4:\n{reshaped}")
    
    # Indexing and slicing
    print(f"\nFirst element: {arr[0]}")  # arr[0] sa C
    print(f"Last element: {arr[-1]}")   # arr[-1] = last element
    print(f"First 5 elements: {arr[:5]}")  # arr[0:5] sa C would be arr[0] to arr[4]
    print(f"Elements 2 to 7: {arr[2:8]}")  # arr[2] to arr[7]
    
    # 2D array indexing
    print(f"\n2D array:\n{reshaped}")
    print(f"Element at row 1, column 2: {reshaped[1, 2]}")  # reshaped[1][2] sa C
    print(f"First row: {reshaped[0, :]}")  # Lahat ng nasa first row
    print(f"Second column: {reshaped[:, 1]}")  # Lahat ng nasa second column
    
except ImportError:
    print("NumPy is not installed. Install it with: pip install numpy")  # I-install mo muna, dali lang yan

# ============================================
# 9. PRACTICAL EXAMPLES
# ============================================

print("\n9. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Grade calculator
# Parang switch-case sa C, pero mas chill

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
# Parang menu sa C, pero mas simple syntax

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
   # Wag tamarin magpangalan ng variable, para di ka malito

2. Write comments to explain your code
   - Use # for single line comments
   - Use ''' or \"\"\" for multi-line comments

3. Use proper indentation (4 spaces)
   - Python is sensitive to indentation
   - Use consistent spacing
   # Indent, indent, indent!

4. Handle errors with try-except
   - Always validate user input
   - Handle potential errors gracefully
   # Para di sumabog program mo pag may mali

5. Use functions to organize code
   - Break complex tasks into smaller functions
   - Make code reusable
   # Para di ka mahirapan mag-debug

6. Use f-strings for string formatting
   - More readable than .format() or %
   - Available in Python 3.6+

7. Use list comprehensions when appropriate
   - More concise than for loops
   - Good for simple transformations
   # One-liner na loop

8. Import libraries at the top of your file
   - Keep imports organized
   - Use specific imports when possible
   # Para di ka maguluhan kung saan galing yung mga gamit mo
""")

print("\n" + "=" * 50)
print("Congratulations! You've completed the Python tutorial for C programmers!")
print("Key differences from C to remember:")
print("- No semicolons needed  # Hindi mo na kailangan ng ; sa dulo")
print("- Use indentation instead of braces  # Indent lang, walang { }")
print("- No need to declare variable types  # Assign ka lang, bahala na si Python")
print("- Lists are dynamic (unlike C arrays)  # Pwede dagdag/bawas kahit kailan")
print("- Functions can return multiple values  # Parang sabay na return, walang struct")
print("- Much more built-in functionality  # Sobrang daming built-in, explore mo lang")
print("Keep practicing and building projects to improve your skills.  # Practice lang nang practice")
print("=" * 50)
