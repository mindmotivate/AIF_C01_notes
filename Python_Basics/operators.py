# Assignment Operator Example

number = 10


# Comparison Example

number_1 = 10
number_2 = 5

if number_1 == number_2:
    print(f"{number_1} is equal to {number_2}.")
else: 
    print(f"{number_1} is not equal to {number_2}.")

if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}.")
else: 
    print(f"{number_1} is less than {number_2}.")


# Membership Example
sequence = [1, 2, 3, 4, 5]

if 3 in sequence:
    print("3 is in the sequence.")
else:
    print("3 is not in the sequence.")


# Logical Operators Example
x = 8
y = 12

if x > 7 and y > 10:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")


# or Operator Example
x = 5
y = 20

if x < 7 or y < 15:
    print("At least one condition is true.")
else:
    print("Both conditions are false.")


# not Operator Example
x = 10

if not (x > 7):
    print("The condition is false.")
else:
    print("The condition is true.")



# Arithmetic Operators Example

# Addition
a = 10
b = 5
sum_result = a + b
print(f"Sum: {sum_result}")

# Subtraction
difference_result = a - b
print(f"Difference: {difference_result}")

# Multiplication
product_result = a * b
print(f"Product: {product_result}")

# Division
division_result = a / b
print(f"Division: {division_result}")

# Modulus
modulus_result = a % b
print(f"Modulus: {modulus_result}")

# Exponentiation
exponentiation_result = a ** b
print(f"Exponentiation: {exponentiation_result}")

# Floor Division
floor_division_result = a // b
print(f"Floor Division: {floor_division_result}")

# String Concatenation
first_name = "John"
last_name = "Doe"
greeting_message = "Hello, " + first_name + " " + last_name + "!"
print(greeting_message)
