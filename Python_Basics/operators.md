# Python Operators

## Assignment Operators

Assignment operators are used to assign values to variables. The most common assignment operator is `=`.

```python
number = 10
```

## Comparison Operators

Comparison operators are used to compare two values and return `True` or `False` based on the result of the comparison. Some common comparison operators include:

- `==` (Equal to)
- `!=` (Not equal to)
- `>` (Greater than)
- `<` (Less than)
- `>=` (Greater than or equal to)
- `<=` (Less than or equal to)


Example:

```python
number_1 = 121
number_2 = 39

if number_1 == number_2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
```

## Membership Operators

Membership operators are used to test whether a value is a member of a sequence (such as a list, tuple, or string). Common membership operators include:

- `in` (Checks if a value is present in a sequence)
- `not in` (Checks if a value is not present in a sequence)

Example:

```python
# sequence = [1, 2, 3, 4, 5]

if 3 in sequence:
    print("3 is in the sequence.")
else:
    print("3 is not in the sequence.")
```

## Logical Operators

Logical operators are used to combine conditional statements and perform logical operations. Common logical operators include:

- `and` (Returns `True` if both conditions are true)
- `or` (Returns `True` if at least one of the conditions is true)
- `not` (Returns `True` if the condition is false)

Example:

```python
a = True
b = False

if a and b:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")
```