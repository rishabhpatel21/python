Name = "Rishabh"
Age = 22
Qualification = "B.E. Computer Engineering"


# About f-strings (formatted string literals):
# f-strings are a way to embed expressions inside string literals, using curly braces `{}`.
# They are prefixed with the letter 'f' or 'F'.
# f-strings are more readable and concise compared to the older string formatting methods.

# Example of using f-strings with variables
print(f"{Name} is {Age} years old and has a qualification of {Qualification}.")
# Output: Rishabh is 22 years old and has a qualification of B.E. Computer Engineering.

# Example of using f-strings with expressions
print(f"{Name} will be {Age + 5} years old in 5 years and will have a qualification of {Qualification.upper()}.")
# Output: Rishabh will be 27 years old in 5 years and will have a qualification of B.E. COMPUTER ENGINEERING.

# f-strings can also be used with dictionaries and lists.
person = {"name": "Rishabh", "age": 22, "qualification": "B.E. Computer Engineering"}
print(f"{person['name']} is {person['age']} years old and has a qualification of {person['qualification']}.")
# Output: Rishabh is 22 years old and has a qualification of B.E. Computer Engineering.

# f-strings can also be used with lists.
fruits = ["apple", "banana", "cherry"]
print(f"My favorite fruits are: {', '.join(fruits)}.")
# Output: My favorite fruits are: apple, banana, cherry