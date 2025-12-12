# Ask user for thier name
#name = input("What's your name? ").strip().title()


# Split user's name into first name and last name
#first, last = name.split(" ")

# Remove whitespaces from str and capitalize user's name
##name = name.strip().title()

#Capitalize user's name
#name = name.capitalize()
#name = name.title()

# Say hello to user
 
# Using the format string 
#print(f"hello, {name}")

 # Using +

#print("hello, "  +  name)  

#Using just the function name
#print("hello,", name)

# Using str

#print("hello, ", end="")
#print(name)



# This is my first python code


# int

 #def is short for define 

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
#print(name)