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
print("\n--- String Examples ---")

# Basic string creation
name = "Alice"  # string, kahit anong text, basta naka-quotes
print(f"Name: {name} (type: {type(name)})")

# String operations and methods
print("\n--- String Operations ---")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition
separator = "-" * 20
print(f"Separator: {separator}")

# String length
message = "Hello, World!"
print(f"Message: '{message}'")
print(f"Length: {len(message)}")

# String indexing and slicing
print(f"First character: {message[0]}")
print(f"Last character: {message[-1]}")
print(f"First 5 characters: {message[:5]}")
print(f"Last 5 characters: {message[-5:]}")
print(f"Characters 7-11: {message[7:12]}")

# String methods
print("\n--- String Methods ---")

# Case conversion
text = "Hello World Python"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# String searching and replacement
sentence = "Python is awesome and Python is fun"
print(f"\nOriginal sentence: {sentence}")
print(f"Contains 'Python': {sentence.count('Python')}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'fun': {sentence.endswith('fun')}")
print(f"Index of 'awesome': {sentence.find('awesome')}")

# String replacement
new_sentence = sentence.replace("Python", "Programming")
print(f"After replacement: {new_sentence}")

# String splitting and joining
print("\n--- String Splitting and Joining ---")

# Split by space
words = sentence.split()
print(f"Words: {words}")

# Split by specific delimiter
csv_data = "apple,banana,orange,grape"
fruits = csv_data.split(",")
print(f"Fruits: {fruits}")

# Join strings
joined_fruits = " | ".join(fruits)
print(f"Joined with ' | ': {joined_fruits}")

# Practical examples
print("\n--- Practical String Examples ---")

# Example 1: Text processing
print("--- Text Processing Example ---")
email_text = """
Dear John,

Thank you for your recent purchase. Your order #12345 has been confirmed.

Best regards,
Customer Service Team
"""

# Clean up the email text
cleaned_text = email_text.strip()  # Remove leading/trailing whitespace
lines = cleaned_text.split('\n')  # Split into lines
non_empty_lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines

print("Cleaned email lines:")
for i, line in enumerate(non_empty_lines, 1):
    print(f"  {i}. {line}")

# Example 2: Data validation
print("\n--- Data Validation Example ---")
def validate_email(email):
    """Basic email validation"""
    if '@' not in email:
        return False, "Missing @ symbol"
    
    if '.' not in email:
        return False, "Missing domain extension"
    
    if len(email) < 5:
        return False, "Email too short"
    
    return True, "Valid email"

test_emails = ["user@email.com", "invalid-email", "short@", "user.email.org"]
for email in test_emails:
    is_valid, message = validate_email(email)
    status = "✓" if is_valid else "✗"
    print(f"{status} {email}: {message}")

# Example 3: Text formatting
print("\n--- Text Formatting Example ---")
product_info = {
    "name": "Laptop",
    "price": 999.99,
    "brand": "TechCorp",
    "rating": 4.5
}

# Create a formatted product description
description = f"""
Product: {product_info['name']}
Brand: {product_info['brand']}
Price: ${product_info['price']:.2f}
Rating: {'★' * int(product_info['rating'])} ({product_info['rating']}/5)
"""

print("Product Description:")
print(description)

# Example 4: Password strength checker
print("--- Password Strength Checker ---")
def check_password_strength(password):
    """Check password strength and provide feedback"""
    feedback = []
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
        feedback.append("✓ Good length (8+ characters)")
    else:
        feedback.append("✗ Too short (need 8+ characters)")
    
    # Uppercase check
    if any(c.isupper() for c in password):
        score += 1
        feedback.append("✓ Contains uppercase letter")
    else:
        feedback.append("✗ Missing uppercase letter")
    
    # Lowercase check
    if any(c.islower() for c in password):
        score += 1
        feedback.append("✓ Contains lowercase letter")
    else:
        feedback.append("✗ Missing lowercase letter")
    
    # Digit check
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("✓ Contains number")
    else:
        feedback.append("✗ Missing number")
    
    # Special character check
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 1
        feedback.append("✓ Contains special character")
    else:
        feedback.append("✗ Missing special character")
    
    # Determine strength
    if score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return strength, score, feedback

# Test passwords
test_passwords = ["weak", "Better123", "StrongP@ss1", "12345678"]
for password in test_passwords:
    strength, score, feedback = check_password_strength(password)
    print(f"\nPassword: '{password}'")
    print(f"Strength: {strength} ({score}/5)")
    for item in feedback:
        print(f"  {item}")

# Example 5: Text analysis
print("\n--- Text Analysis Example ---")
sample_text = """
Python is a high-level programming language known for its simplicity and readability.
It was created by Guido van Rossum and first released in 1991. Python supports
multiple programming paradigms including procedural, object-oriented, and functional programming.
"""

# Analyze the text
words = sample_text.lower().split()
word_count = len(words)
unique_words = len(set(words))
char_count = len(sample_text.replace(" ", "").replace("\n", ""))

# Find most common words
from collections import Counter
word_freq = Counter(words)
most_common = word_freq.most_common(5)

print("Text Analysis:")
print(f"Total words: {word_count}")
print(f"Unique words: {unique_words}")
print(f"Character count (no spaces): {char_count}")
print(f"Most common words: {most_common}")

# Example 6: String formatting for reports
print("\n--- Report Formatting Example ---")
sales_data = [
    ("Product A", 150, 25.99),
    ("Product B", 89, 15.50),
    ("Product C", 200, 8.75),
    ("Product D", 75, 32.00)
]

# Create a formatted sales report
print("SALES REPORT")
print("=" * 50)
print(f"{'Product':<15} {'Quantity':<10} {'Price':<10} {'Total':<10}")
print("-" * 50)

total_revenue = 0
for product, quantity, price in sales_data:
    total = quantity * price
    total_revenue += total
    print(f"{product:<15} {quantity:<10} ${price:<9.2f} ${total:<9.2f}")

print("-" * 50)
print(f"{'TOTAL REVENUE':<35} ${total_revenue:<9.2f}")
print("=" * 50)

# Boolean
is_student = True # naka capitalized talaga dapat yang T, wag mo kalimutan!
print(f"Is student: {is_student} (type: {type(is_student)})")

# List - dynamic array
fruits = ["apple", "banana", "orange"]  # parang array, pero pwede dagdag/bawas kahit kailan
print(f"Fruits: {fruits} (type: {type(fruits)})")

# Tuple - immutable list (like const array in C)
print("\n--- Tuple Examples ---")

# Basic tuple creation
coordinates = (10, 20)  # parang array na di mo na pwede baguhin
print(f"Coordinates: {coordinates} (type: {type(coordinates)})")

# Tuple unpacking (very useful!)
x, y = coordinates
print(f"X coordinate: {x}, Y coordinate: {y}")

# Tuple for multiple return values from functions
def get_person_info():
    return "Alice", 25, "Engineer"  # Returns a tuple

name, age, job = get_person_info()
print(f"Person: {name}, Age: {age}, Job: {job}")

# Tuple for coordinates and dimensions
print("\n--- Coordinate and Dimension Examples ---")
rectangle = (100, 50)  # width, height
width, height = rectangle
area = width * height
print(f"Rectangle: {width} x {height} = {area} square units")

# Multiple points
points = [(0, 0), (1, 1), (2, 4), (3, 9)]
print("Points on a curve:")
for x, y in points:
    print(f"  ({x}, {y})")

# Tuple for RGB colors
print("\n--- Color Examples ---")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

print(f"Red: {red}")
print(f"Green: {green}")
print(f"Blue: {blue}")

# Mix colors (simple average)
def mix_colors(color1, color2):
    """Mix two RGB colors by averaging their components"""
    r = (color1[0] + color2[0]) // 2
    g = (color1[1] + color2[1]) // 2
    b = (color1[2] + color2[2]) // 2
    return (r, g, b)

purple = mix_colors(red, blue)
print(f"Red + Blue = Purple: {purple}")

# Tuple for database records
print("\n--- Database Record Examples ---")
users = [
    ("alice", "alice@email.com", "admin"),
    ("bob", "bob@email.com", "user"),
    ("charlie", "charlie@email.com", "moderator")
]

print("User records:")
for username, email, role in users:
    print(f"  {username}: {email} ({role})")

# Tuple for configuration settings
print("\n--- Configuration Examples ---")
server_config = ("localhost", 8080, True)  # host, port, debug
host, port, debug = server_config
print(f"Server: {host}:{port}, Debug: {debug}")

# Tuple for date/time
print("\n--- Date/Time Examples ---")
from datetime import datetime
now = datetime.now()
current_time = (now.hour, now.minute, now.second)
print(f"Current time: {current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d}")

# Tuple for mathematical operations
print("\n--- Mathematical Examples ---")
def quadratic_roots(a, b, c):
    """Calculate roots of quadratic equation ax² + bx + c = 0"""
    import math
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root, root)
    else:
        return None  # Complex roots

# Test quadratic equation: x² - 5x + 6 = 0
roots = quadratic_roots(1, -5, 6)
if roots:
    print(f"Roots of x² - 5x + 6 = 0: {roots}")
else:
    print("Complex roots")

# Tuple for coordinates in 3D space
print("\n--- 3D Coordinate Examples ---")
cube_vertices = [
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),  # bottom face
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)   # top face
]

print("Cube vertices:")
for i, (x, y, z) in enumerate(cube_vertices):
    print(f"  Vertex {i}: ({x}, {y}, {z})")

# Calculate center of cube
center_x = sum(x for x, y, z in cube_vertices) / len(cube_vertices)
center_y = sum(y for x, y, z in cube_vertices) / len(cube_vertices)
center_z = sum(z for x, y, z in cube_vertices) / len(cube_vertices)
center = (center_x, center_y, center_z)
print(f"Cube center: {center}")

# Tuple for named constants
print("\n--- Named Constants Examples ---")
# Instead of using magic numbers, use descriptive tuples
PI = 3.14159
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458

# Physical constants
PHYSICAL_CONSTANTS = (PI, GRAVITY, SPEED_OF_LIGHT)
print(f"Physical constants: π={PHYSICAL_CONSTANTS[0]}, g={PHYSICAL_CONSTANTS[1]}, c={PHYSICAL_CONSTANTS[2]}")

# Tuple for data validation
print("\n--- Data Validation Examples ---")
def validate_coordinates(x, y, z):
    """Validate that coordinates are within valid ranges"""
    min_val = -1000
    max_val = 1000
    
    if min_val <= x <= max_val and min_val <= y <= max_val and min_val <= z <= max_val:
        return (True, "Valid coordinates")
    else:
        return (False, "Coordinates out of range")

# Test validation
test_coords = [(100, 200, 300), (1500, 0, 0), (-500, 600, 700)]
for x, y, z in test_coords:
    is_valid, message = validate_coordinates(x, y, z)
    status = "✓" if is_valid else "✗"
    print(f"{status} ({x}, {y}, {z}): {message}")

# Dictionary - hash table (like struct with key-value pairs)
print("\n--- Dictionary Examples ---")

# Basic dictionary creation
person = {"name": "Bob", "age": 30, "city": "New York"}
print(f"Person: {person} (type: {type(person)})")

# Dictionary operations - adding, updating, removing
print("\n--- Dictionary Operations ---")

# Adding new key-value pairs
person["email"] = "bob@email.com"
person["phone"] = "555-1234"
print(f"After adding email and phone: {person}")

# Updating existing values
person["age"] = 31  # Bob had a birthday!
print(f"After updating age: {person}")

# Removing items
removed_phone = person.pop("phone")  # Remove and get the value
print(f"Removed phone: {removed_phone}")
print(f"After removing phone: {person}")

# Checking if key exists
if "email" in person:
    print(f"Email found: {person['email']}")
else:
    print("Email not found")

# Safe way to get values (won't crash if key doesn't exist)
city = person.get("city", "Unknown")  # Default value if key doesn't exist
print(f"City: {city}")

# Dictionary methods
print(f"\nAll keys: {list(person.keys())}")
print(f"All values: {list(person.values())}")
print(f"All items: {list(person.items())}")

# Practical example: Student grade book
print("\n--- Student Grade Book Example ---")
grade_book = {
    "Alice": {"math": 95, "science": 88, "english": 92},
    "Bob": {"math": 78, "science": 85, "english": 90},
    "Charlie": {"math": 92, "science": 95, "english": 87}
}

# Adding a new student
grade_book["Diana"] = {"math": 88, "science": 91, "english": 94}

# Updating grades
grade_book["Bob"]["math"] = 82  # Bob improved in math!

# Calculating averages
for student, grades in grade_book.items():
    average = sum(grades.values()) / len(grades)
    print(f"{student}: {grades} -> Average: {average:.1f}")

# Finding the best student in each subject
subjects = ["math", "science", "english"]
for subject in subjects:
    best_student = max(grade_book.keys(), key=lambda s: grade_book[s][subject])
    best_score = grade_book[best_student][subject]
    print(f"Best in {subject}: {best_student} with {best_score}")

# Dictionary comprehension example
print("\n--- Dictionary Comprehension ---")
# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Create a dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age_dict = {name: age for name, age in zip(names, ages)}
print(f"Name-age dictionary: {name_age_dict}")

# Nested dictionaries for complex data
print("\n--- Nested Dictionary Example ---")
company = {
    "name": "TechCorp",
    "employees": {
        "IT": {
            "Alice": {"position": "Developer", "salary": 75000, "skills": ["Python", "JavaScript"]},
            "Bob": {"position": "DevOps", "salary": 80000, "skills": ["Docker", "AWS"]}
        },
        "HR": {
            "Charlie": {"position": "Manager", "salary": 65000, "skills": ["Recruitment", "Training"]}
        }
    },
    "departments": ["IT", "HR", "Finance"]
}

# Accessing nested data
print(f"Company: {company['name']}")
print(f"Alice's position: {company['employees']['IT']['Alice']['position']}")
print(f"Alice's skills: {company['employees']['IT']['Alice']['skills']}")

# Adding new employee
company['employees']['IT']['Diana'] = {
    "position": "Data Scientist", 
    "salary": 85000, 
    "skills": ["Python", "Machine Learning", "SQL"]
}

# List all IT employees and their skills
print("\nIT Department Employees:")
for name, info in company['employees']['IT'].items():
    skills_str = ", ".join(info['skills'])
    print(f"  {name}: {info['position']} - Skills: {skills_str}")

# Dictionary as function parameters
print("\n--- Dictionary as Function Parameters ---")

def create_person_profile(**kwargs):
    """Create a person profile from keyword arguments"""
    profile = {
        "name": kwargs.get("name", "Unknown"),
        "age": kwargs.get("age", 0),
        "occupation": kwargs.get("occupation", "Unemployed"),
        "hobbies": kwargs.get("hobbies", [])
    }
    return profile

# Using the function with different parameters
person1 = create_person_profile(name="Alice", age=25, occupation="Engineer")
person2 = create_person_profile(name="Bob", age=30, occupation="Teacher", hobbies=["reading", "hiking"])

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")

# Dictionary for configuration
print("\n--- Configuration Dictionary ---")
app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db",
        "user": "admin"
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": True
    },
    "features": {
        "enable_logging": True,
        "max_connections": 100,
        "timeout": 30
    }
}

# Accessing configuration
db_host = app_config["database"]["host"]
server_port = app_config["server"]["port"]
print(f"Database host: {db_host}")
print(f"Server port: {server_port}")

# Updating configuration
app_config["server"]["debug"] = False
print(f"Debug mode: {app_config['server']['debug']}")

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

print("\n--- Advanced Function Examples ---")

# Example 1: Calculator functions
print("--- Calculator Functions ---")
def calculate(operation, a, b):
    """Perform basic arithmetic operations"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Test calculator
operations = ["add", "subtract", "multiply", "divide"]
for op in operations:
    result = calculate(op, 10, 5)
    print(f"10 {op} 5 = {result}")

# Example 2: Data processing functions
print("\n--- Data Processing Functions ---")
def analyze_numbers(numbers):
    """Analyze a list of numbers and return statistics"""
    if not numbers:
        return None
    
    stats = {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "even_count": len([x for x in numbers if x % 2 == 0]),
        "odd_count": len([x for x in numbers if x % 2 != 0])
    }
    
    # Calculate standard deviation
    mean = stats["average"]
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    stats["std_dev"] = variance ** 0.5
    
    return stats

# Test number analysis
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
analysis = analyze_numbers(test_numbers)
print(f"Analysis of {test_numbers}:")
for key, value in analysis.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# Example 3: File processing functions
print("\n--- File Processing Functions ---")
def process_text_file(filename, operation="read"):
    """Process text files with different operations"""
    try:
        if operation == "read":
            with open(filename, 'r') as file:
                content = file.read()
                return content
        elif operation == "count_words":
            with open(filename, 'r') as file:
                content = file.read()
                words = content.split()
                return len(words)
        elif operation == "count_lines":
            with open(filename, 'r') as file:
                lines = file.readlines()
                return len(lines)
        else:
            return "Error: Invalid operation"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {str(e)}"

# Example 4: Recursive functions
print("\n--- Recursive Functions ---")
def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci number using recursion"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test recursive functions
print("Factorial examples:")
for i in range(6):
    print(f"  {i}! = {factorial(i)}")

print("Fibonacci sequence:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

# Example 5: Higher-order functions
print("\n--- Higher-Order Functions ---")
def apply_operation(func, numbers):
    """Apply a function to a list of numbers"""
    return [func(num) for num in numbers]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def is_even(x):
    return x % 2 == 0

# Test higher-order functions
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")
print(f"Squared: {apply_operation(square, numbers)}")
print(f"Cubed: {apply_operation(cube, numbers)}")
print(f"Even numbers: {[x for x in numbers if is_even(x)]}")

# Example 6: Lambda functions (anonymous functions)
print("\n--- Lambda Functions ---")
# Lambda functions are like inline functions
double = lambda x: x * 2
add = lambda x, y: x + y
is_positive = lambda x: x > 0

print(f"Double of 5: {double(5)}")
print(f"Add 3 and 7: {add(3, 7)}")
print(f"Is 10 positive? {is_positive(10)}")
print(f"Is -5 positive? {is_positive(-5)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(f"Even numbers: {even_numbers}")
print(f"Squared numbers: {squared_numbers}")

# Example 7: Decorator functions
print("\n--- Decorator Functions ---")
def timer(func):
    """Decorator to measure function execution time"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """A function that takes some time to execute"""
    import time
    time.sleep(1)  # Simulate work
    return "Done!"

# Test decorator
result = slow_function()
print(f"Result: {result}")

# Example 8: Generator functions
print("\n--- Generator Functions ---")
def number_generator(start, end, step=1):
    """Generate numbers from start to end with given step"""
    current = start
    while current <= end:
        yield current
        current += step

def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Test generators
print("Number generator (1 to 10, step 2):")
for num in number_generator(1, 10, 2):
    print(f"  {num}", end="")
print()  # New line

print("First 10 Fibonacci numbers:")
for fib in fibonacci_generator(10):
    print(f"  {fib}", end="")
print()  # New line

# Example 9: Error handling in functions
print("\n--- Error Handling in Functions ---")
def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both arguments must be numbers"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Test error handling
test_cases = [(10, 2), (10, 0), ("10", 2), (10, "2")]
for a, b in test_cases:
    result = safe_divide(a, b)
    print(f"safe_divide({a}, {b}) = {result}")

# Example 10: Function with variable arguments
print("\n--- Variable Arguments Functions ---")
def calculate_total(*args, **kwargs):
    """Calculate total with variable arguments and keyword arguments"""
    total = sum(args)
    
    # Apply discounts from keyword arguments
    if 'discount' in kwargs:
        discount = kwargs['discount']
        total = total * (1 - discount)
    
    if 'tax_rate' in kwargs:
        tax_rate = kwargs['tax_rate']
        total = total * (1 + tax_rate)
    
    return total

# Test variable arguments
print(f"Total (10, 20, 30): ${calculate_total(10, 20, 30):.2f}")
print(f"Total with 10% discount: ${calculate_total(10, 20, 30, discount=0.1):.2f}")
print(f"Total with 10% discount and 8% tax: ${calculate_total(10, 20, 30, discount=0.1, tax_rate=0.08):.2f}")

# ============================================
# 7. LISTS AND LIST METHODS
# ============================================

print("\n7. LISTS AND LIST METHODS")
print("-" * 30)

# Creating lists
numbers = [1, 2, 3, 4, 5]
colors = ["red", "green", "blue"]

print("--- Basic List Operations ---")
# Adding elements
numbers.append(6)  # Add to end
print(f"After append: {numbers}")

numbers.insert(0, 0)  # Insert at specific position, insert sa simula
print(f"After insert: {numbers}")

# Removing elements
numbers.remove(3)  # Remove specific value, hanapin niya tapos tanggalin
print(f"After remove: {numbers}")

popped = numbers.pop()  # Remove and return last element
print(f"Popped: {popped}, List: {numbers}")

# List operations
print(f"Length: {len(numbers)}")  # Gusto mo malaman ilang laman? len() lang!
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")     # Total ng lahat

# List comprehension (advanced but useful)
squares = [x**2 for x in range(5)]  # Gawa agad ng list ng squares, parang loop na one-liner
print(f"Squares: {squares}")

print("\n--- Practical List Examples ---")

# Example 1: Shopping Cart
print("--- Shopping Cart Example ---")
shopping_cart = []
shopping_cart.append({"item": "Laptop", "price": 999.99, "quantity": 1})
shopping_cart.append({"item": "Mouse", "price": 25.50, "quantity": 2})
shopping_cart.append({"item": "Keyboard", "price": 75.00, "quantity": 1})

print("Shopping Cart:")
for item in shopping_cart:
    total = item["price"] * item["quantity"]
    print(f"  {item['item']} x{item['quantity']} - ${item['price']:.2f} = ${total:.2f}")

# Calculate total
cart_total = sum(item["price"] * item["quantity"] for item in shopping_cart)
print(f"Total: ${cart_total:.2f}")

# Example 2: Student Management System
print("\n--- Student Management System ---")
students = [
    {"name": "Alice", "grades": [95, 88, 92], "attendance": 95},
    {"name": "Bob", "grades": [78, 85, 90], "attendance": 88},
    {"name": "Charlie", "grades": [92, 95, 87], "attendance": 92}
]

# Add new student
students.append({"name": "Diana", "grades": [88, 91, 94], "attendance": 96})

# Calculate averages and find top performers
for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    student["average"] = round(avg_grade, 1)
    print(f"{student['name']}: Grades {student['grades']} -> Average: {student['average']}")

# Find student with highest average
top_student = max(students, key=lambda s: s["average"])
print(f"\nTop student: {top_student['name']} with average {top_student['average']}")

# Example 3: Task Management
print("\n--- Task Management System ---")
tasks = [
    {"id": 1, "title": "Complete Python tutorial", "priority": "High", "completed": False},
    {"id": 2, "title": "Review code", "priority": "Medium", "completed": True},
    {"id": 3, "title": "Write documentation", "priority": "Low", "completed": False}
]

# Add new task
tasks.append({"id": 4, "title": "Test application", "priority": "High", "completed": False})

# Mark task as completed
for task in tasks:
    if task["title"] == "Complete Python tutorial":
        task["completed"] = True
        break

# Filter tasks by status
pending_tasks = [task for task in tasks if not task["completed"]]
completed_tasks = [task for task in tasks if task["completed"]]

print("Pending tasks:")
for task in pending_tasks:
    print(f"  [{task['priority']}] {task['title']}")

print("Completed tasks:")
for task in completed_tasks:
    print(f"  ✓ {task['title']}")

# Example 4: Data Processing
print("\n--- Data Processing Example ---")
# Simulate sensor readings
sensor_readings = [23.5, 24.1, 23.8, 25.2, 24.9, 23.3, 26.1, 25.8]

# Calculate statistics
avg_temp = sum(sensor_readings) / len(sensor_readings)
max_temp = max(sensor_readings)
min_temp = min(sensor_readings)

print(f"Temperature readings: {sensor_readings}")
print(f"Average: {avg_temp:.1f}°C")
print(f"Maximum: {max_temp}°C")
print(f"Minimum: {min_temp}°C")

# Find readings above average
above_avg = [temp for temp in sensor_readings if temp > avg_temp]
print(f"Readings above average: {above_avg}")

# Example 5: List Manipulation Techniques
print("\n--- Advanced List Techniques ---")

# Sorting
numbers_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {numbers_list}")

# Sort in ascending order
ascending = sorted(numbers_list)
print(f"Ascending: {ascending}")

# Sort in descending order
descending = sorted(numbers_list, reverse=True)
print(f"Descending: {descending}")

# Sort by custom criteria (e.g., by last digit)
by_last_digit = sorted(numbers_list, key=lambda x: x % 10)
print(f"By last digit: {by_last_digit}")

# Filtering with conditions
even_numbers = [x for x in numbers_list if x % 2 == 0]
odd_numbers = [x for x in numbers_list if x % 2 != 0]
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")

# List slicing examples
print(f"\nOriginal list: {numbers_list}")
print(f"First 3 elements: {numbers_list[:3]}")
print(f"Last 3 elements: {numbers_list[-3:]}")
print(f"Middle elements (2-5): {numbers_list[1:5]}")
print(f"Every 2nd element: {numbers_list[::2]}")
print(f"Reverse list: {numbers_list[::-1]}")

# Combining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"\nCombined lists: {list1} + {list2} = {combined}")

# Extending a list
list1.extend([7, 8, 9])
print(f"After extend: {list1}")

# Copying lists (avoiding reference issues)
original = [1, 2, 3]
copy1 = original.copy()  # Shallow copy
copy2 = original[:]      # Slice copy
copy3 = list(original)   # List constructor copy

original[0] = 99
print(f"Original: {original}")
print(f"Copy 1: {copy1}")
print(f"Copy 2: {copy2}")
print(f"Copy 3: {copy3}")

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
