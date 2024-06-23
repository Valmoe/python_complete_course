"""
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 5 characters long
    name can be a maximum of 5 characters
otherwise
    looks good!
"""
name = input("Enter you name: ")
print(name)
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 5:
    print("name cannot be more than 5 characters")
else:
    print("looks good!")