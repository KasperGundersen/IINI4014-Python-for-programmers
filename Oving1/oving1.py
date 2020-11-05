# Allows user to enter their full name
name = input("Please enter your name:\n")

# Splits full name into separate names

names = name.split()
initials = []

# Adding the first letter in every seperate name to the initials-list
for n in names:
    initials.append(n[0])

# Joining the initials to one word
i = ''.join(initials)

print(f'Welcome to Python for programmers {name}\nYour initials are {i}')

    