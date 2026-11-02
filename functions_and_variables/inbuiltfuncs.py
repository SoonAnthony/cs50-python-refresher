name = input("What's your name?")
name = name.strip().title()
# to split the name into first and last name
first, last = name.split(" ")
print(f"Hello, {name}!")
print (f"Hello, your first name is {first} and your last name is {last}.")


